"""
Extended geometric diagnostics on a real NS field (single GPU, N=128).
Measures in one run, over a STATIONARY window (warmup then sample at
steps ~3000-6000; NOT a long run, since long runs relax — lesson from D1):

  [U5] Intermittency directly in the data: PDF and flatness of |grad u|
       per class (C_small/C_free/C_large) and for the full field.
       Tests whether non-Gaussian heavy tails exist in the classes
       themselves (independent of the 3-state model, which failed to
       reproduce them from measured parameters).
  [U1] Onsager bridge measured: energy-flux density
       Pi = -tr(e^3) - (1/4) omega.e.omega, averaged per class.
       Checks the analytic claim that C_free carries ~zero flux.
  [U2] Lifetime scaling: class fractions per octave band (proxy for the
       scale dependence of the geometry).
  [U3] Vorticity-strain alignment |cos(omega,e_i)| per class.

Run:  py -3.12 diag.py          # full
      py -3.12 diag.py --test   # quick N=16 sanity
Output: diag_results.json. Send it back.
"""
import torch, numpy as np, json, time, sys

TESTONLY='--test' in sys.argv
device='cuda' if torch.cuda.is_available() else 'cpu'
dtype,ctype=torch.float32,torch.complex64
N=16 if TESTONLY else 128
nu=0.02 if TESTONLY else 0.006
dt=0.01 if TESTONLY else 0.0015
force_k=2; force_eps=0.12
warmup=40 if TESTONLY else 3000
n_sample=3 if TESTONLY else 8         # snapshots within stationary window
sample_gap=10 if TESTONLY else 350
torch.manual_seed(0)

k1=torch.fft.fftfreq(N,d=1.0/N).to(device)
KX,KY,KZ=torch.meshgrid(k1,k1,k1,indexing='ij')
K2=KX**2+KY**2+KZ**2; K2c=K2.clone(); K2c[0,0,0]=1.0
Kmag=torch.sqrt(K2); kmax=N//3
dealias=((torch.abs(KX)<=kmax)&(torch.abs(KY)<=kmax)&(torch.abs(KZ)<=kmax)).to(dtype)
Kl=[KX,KY,KZ]

def project(uk):
    div=KX*uk[0]+KY*uk[1]+KZ*uk[2]
    return torch.stack([uk[0]-KX*div/K2c,uk[1]-KY*div/K2c,uk[2]-KZ*div/K2c])
def init_field():
    a=torch.randn(3,N,N,N,dtype=dtype,device=device)
    ak=torch.fft.fftn(a,dim=(1,2,3)).to(ctype)
    env=(Kmag**2)*torch.exp(-(Kmag/4.0)**2); env=env/(env.max()+1e-12)
    return project(ak*env)
def nonlinear(uk):
    u=torch.fft.ifftn(uk,dim=(1,2,3)).real
    ok=torch.stack([1j*(KY*uk[2]-KZ*uk[1]),1j*(KZ*uk[0]-KX*uk[2]),1j*(KX*uk[1]-KY*uk[0])])
    om=torch.fft.ifftn(ok,dim=(1,2,3)).real
    c=torch.stack([u[1]*om[2]-u[2]*om[1],u[2]*om[0]-u[0]*om[2],u[0]*om[1]-u[1]*om[0]])
    return project(torch.fft.fftn(c,dim=(1,2,3)).to(ctype)*dealias)
def forcing(uk):
    shell=(Kmag>0)&(Kmag<=force_k)
    e=float(torch.sum(torch.abs(uk[:,shell])**2).real)
    if e<1e-10: return torch.zeros_like(uk)
    g=min(max((force_eps/(e+1e-12))**0.5,0.8),1.25)
    f=torch.zeros_like(uk); f[:,shell]=(g-1.0)*uk[:,shell]; return f
def step(uk):
    visc=torch.exp(-nu*K2*dt)
    Nk=nonlinear(uk)+forcing(uk); u1=(uk+dt*Nk)*visc
    N1=nonlinear(u1)+forcing(u1)
    return project((uk*visc)+0.5*dt*(Nk*visc+N1*visc))

def gradu(uk):
    g=torch.empty(3,3,N,N,N,device=device,dtype=dtype)
    for i in range(3):
        for j in range(3):
            g[i,j]=torch.fft.ifftn(1j*Kl[j]*uk[i],dim=(0,1,2)).real
    return g

def classify_field(g):
    e=0.5*(g+g.transpose(0,1))
    em=e.permute(2,3,4,0,1).reshape(-1,3,3)
    w,v=torch.linalg.eigh(em)               # ascending
    l3,l2,l1=w[:,0],w[:,1],w[:,2]
    denom=(l1**2+l2**2+l3**2)**1.5+1e-12
    s=-3*np.sqrt(6)*(l1*l2*l3)/denom
    cls=torch.full((em.shape[0],),2,device=device,dtype=torch.long)
    free=(torch.abs(s)<0.5)
    small=(l1>1.6*torch.abs(l3))&(~free)
    cls[free]=1; cls[small]=0
    return cls,e,em,w,v

def measure(uk):
    g=gradu(uk)
    cls,e,em,w,v=classify_field(g)
    gradnorm=torch.linalg.matrix_norm(em)         # |grad u| per point
    # vorticity
    om=torch.stack([g[2,1]-g[1,2],g[0,2]-g[2,0],g[1,0]-g[0,1]])
    omf=om.permute(1,2,3,0).reshape(-1,3)
    omn=omf/(torch.linalg.norm(omf,dim=1,keepdim=True)+1e-12)
    res={}
    # [U5] flatness of |grad u| overall and per class
    def flat(x):
        x=x-x.mean(); m2=(x**2).mean(); m4=(x**4).mean()
        return float(m4/(m2**2+1e-12))
    res['flatness_full']=flat(gradnorm)
    res['flatness_per_class']=[flat(gradnorm[cls==i]) if (cls==i).sum()>10 else None for i in range(3)]
    res['mean_gradnorm_per_class']=[float(gradnorm[cls==i].mean()) if (cls==i).sum()>10 else None for i in range(3)]
    # [U1] energy flux density per class
    tr_e3=torch.einsum('pij,pjk,pki->p',em,em,em)
    wew=torch.einsum('pi,pij,pj->p',omn*torch.linalg.norm(omf,dim=1,keepdim=True),em,
                     omn*torch.linalg.norm(omf,dim=1,keepdim=True))
    Pi=-tr_e3-0.25*wew
    res['flux_per_class']=[float(Pi[cls==i].mean()) if (cls==i).sum()>10 else None for i in range(3)]
    res['flux_full']=float(Pi.mean())
    # [U3] alignment |cos(omega,e_i)| per class
    cos1=torch.abs(torch.sum(omn*v[:,:,2],dim=1))
    cos2=torch.abs(torch.sum(omn*v[:,:,1],dim=1))
    cos3=torch.abs(torch.sum(omn*v[:,:,0],dim=1))
    res['align_e1_per_class']=[float(cos1[cls==i].mean()) if (cls==i).sum()>10 else None for i in range(3)]
    res['align_e2_per_class']=[float(cos2[cls==i].mean()) if (cls==i).sum()>10 else None for i in range(3)]
    res['align_e3_per_class']=[float(cos3[cls==i].mean()) if (cls==i).sum()>10 else None for i in range(3)]
    res['occ']=[float((cls==i).float().mean()) for i in range(3)]
    # [U2] class fraction per octave (scale dependence)
    octs=[(4,8),(8,16),(16,32)] if N>=64 else [(2,4),(4,8)]
    phi_oct=[]
    for lo,hi in octs:
        band=((Kmag>=lo)&(Kmag<hi)).to(dtype)
        ukf=uk*band
        gf=gradu(ukf)
        clsf,_,_,_,_=classify_field(gf)
        phi_oct.append([float((clsf==i).float().mean()) for i in range(3)])
    res['octave_class_fractions']=phi_oct
    res['octaves']=octs
    return res

def main():
    uk=init_field(); t0=time.time()
    print(f"device={device} N={N} warmup={warmup}")
    for it in range(warmup):
        uk=step(uk)
        if it%max(1,warmup//4)==0:
            E=float((torch.fft.ifftn(uk,dim=(1,2,3)).real**2).sum().real)*0.5/N**3
            print(f"  warmup {it}/{warmup} E={E:.3e}")
            if not np.isfinite(E): print("blow-up"); return
    print("sampling stationary window...")
    samples=[]
    for s in range(n_sample):
        for _ in range(sample_gap): uk=step(uk)
        samples.append(measure(uk))
        print(f"  sample {s+1}/{n_sample} t={time.time()-t0:.0f}s")
    # aggregate
    def col(key):
        return [x[key] for x in samples]
    def avg_list(key):
        arr=np.array([[v if v is not None else np.nan for v in x[key]] for x in samples])
        return np.nanmean(arr,axis=0).tolist()
    out=dict(N=N, n_samples=len(samples),
        flatness_full=float(np.mean(col('flatness_full'))),
        flatness_per_class=avg_list('flatness_per_class'),
        mean_gradnorm_per_class=avg_list('mean_gradnorm_per_class'),
        flux_full=float(np.mean(col('flux_full'))),
        flux_per_class=avg_list('flux_per_class'),
        align_e1_per_class=avg_list('align_e1_per_class'),
        align_e2_per_class=avg_list('align_e2_per_class'),
        align_e3_per_class=avg_list('align_e3_per_class'),
        occ=avg_list('occ'),
        octaves=samples[0]['octaves'],
        octave_class_fractions=np.array([x['octave_class_fractions'] for x in samples]).mean(0).tolist(),
        class_order=["C_small","C_free","C_large"])
    json.dump(out,open('diag_results.json','w'),indent=2)
    print("\n=== SUMMARY ===")
    print(f"flatness full={out['flatness_full']:.2f} (Gaussian=3, >3 intermittent)")
    print(f"flatness/class {np.round(out['flatness_per_class'],2)}  [small,free,large]")
    print(f"flux/class     {np.round(out['flux_per_class'],4)}  (C_free ~0 expected)")
    print(f"align e2/class {np.round(out['align_e2_per_class'],3)}  (>0.5 = omega aligns intermediate)")
    print(f"occupancy      {np.round(out['occ'],3)}")
    print("Saved diag_results.json — send it back.")

if __name__=='__main__':
    if TESTONLY: print("SELF-TEST N=16"); main(); print("self-test done")
    else: main()
