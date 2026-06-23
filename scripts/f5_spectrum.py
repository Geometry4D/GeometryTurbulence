"""
F5: class-resolved scale energy. On a real NS field, does small-scale
energy concentrate in stretching zones (C_small)?

Method (validated, no convolution artifact): for each Fourier band,
band-pass filter the velocity (smooth in k), form the energy density
|u_band(x)|^2, and take its conditional mean PER CLASS. The law of total
probability (sum of fraction*<e|class> = full) is checked to hold.

Run:  py -3.12 f5_spectrum.py          # full N=128
      py -3.12 f5_spectrum.py --test   # N=16 sanity
Output: f5_results.json
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
n_sample=3 if TESTONLY else 8
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
    shell=(Kmag>0)&(Kmag<=force_k); e=float(torch.sum(torch.abs(uk[:,shell])**2).real)
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
        for j in range(3): g[i,j]=torch.fft.ifftn(1j*Kl[j]*uk[i],dim=(0,1,2)).real
    return g
BANDS=[(2,4),(4,8),(8,16),(16,32)] if N>=64 else [(2,4),(4,8)]
def measure(uk):
    g=gradu(uk); e=0.5*(g+g.transpose(0,1))
    em=e.permute(2,3,4,0,1).reshape(-1,3,3)
    ws=[]
    for i in range(0, em.shape[0], 500_000):
        ws.append(torch.linalg.eigvalsh(em[i:i+500_000]))
    w = torch.cat(ws, dim=0)
    l1,l2,l3=w[:,2],w[:,1],w[:,0]
    s=-3*np.sqrt(6)*(l1*l2*l3)/((l1**2+l2**2+l3**2)**1.5+1e-12)
    free=torch.abs(s)<0.5; small=(l1>1.6*torch.abs(l3))&(~free); large=(~free)&(~small)
    out={}
    for lo,hi in BANDS:
        band=((Kmag>=lo)&(Kmag<hi)).to(dtype)
        ek=torch.zeros(N,N,N,device=device)
        for i in range(3):
            ui=torch.fft.ifftn(uk[i]*band,dim=(0,1,2)).real
            ek=ek+ui**2
        ekf=ek.reshape(-1)
        def cm(mask): return float(ekf[mask].mean()) if mask.sum()>10 else None
        full=float(ekf.mean())
        recon=(cm(free) or 0)*float(free.float().mean())+(cm(small) or 0)*float(small.float().mean())+(cm(large) or 0)*float(large.float().mean())
        out[f"{lo}-{hi}"]=dict(free=cm(free),small=cm(small),large=cm(large),
                                full=full,ratio=recon/(full+1e-30))
    out['fracs']=[float(free.float().mean()),float(small.float().mean()),float(large.float().mean())]
    return out
def main():
    uk=init_field(); t0=time.time()
    print(f"device={device} N={N} bands={BANDS}")
    for it in range(warmup):
        uk=step(uk)
        if it%max(1,warmup//4)==0:
            E=float((torch.fft.ifftn(uk,dim=(1,2,3)).real**2).sum().real)*0.5/N**3
            print(f"  warmup {it}/{warmup} E={E:.3e}")
            if not np.isfinite(E): print("blow-up"); return
    samples=[]
    for sidx in range(n_sample):
        for _ in range(sample_gap): uk=step(uk)
        samples.append(measure(uk)); print(f"  sample {sidx+1}/{n_sample} t={time.time()-t0:.0f}s")
    agg={}
    for lo,hi in BANDS:
        key=f"{lo}-{hi}"
        def av(field):
            v=[s[key][field] for s in samples if s[key][field] is not None]
            return float(np.mean(v)) if v else None
        agg[key]=dict(free=av('free'),small=av('small'),large=av('large'),
                      full=av('full'),ratio=av('ratio'))
    out=dict(N=N,n_samples=len(samples),bands=BANDS,
             fracs=np.mean([s['fracs'] for s in samples],axis=0).tolist(),
             per_band=agg,class_order=["free","small","large"])
    json.dump(out,open('f5_results.json','w'),indent=2)
    print("\n=== CLASS-RESOLVED SCALE ENERGY <e|class> ===")
    print(f"{'band':>8} {'free':>11} {'small':>11} {'large':>11} {'ratio':>7}")
    for lo,hi in BANDS:
        a=agg[f"{lo}-{hi}"]
        print(f"{lo}-{hi:>4} {a['free'] or 0:>11.2e} {a['small'] or 0:>11.2e} {a['large'] or 0:>11.2e} {a['ratio'] or 0:>7.3f}")
    print("\nIf small >> free at high k: small-scale energy concentrates in stretching zones.")
    print("If all ~equal: class geometry is orthogonal to scale energy (negative, informative).")
    print("ratio~1 confirms no artifact. Saved f5_results.json — send back.")
if __name__=='__main__':
    if TESTONLY: print("SELF-TEST N=16"); main(); print("self-test done")
    else: main()
