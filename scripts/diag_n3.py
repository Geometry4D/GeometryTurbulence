"""
N3: robustness of the energy-flux bridge (C_free ~ zero flux) to the
classification threshold. Single GPU, N=128, stationary window.

Recomputes per-class flux Pi = -tr(e^3) - (1/4) omega.e.omega for a RANGE
of shape-parameter thresholds |s|<thr defining C_free. If C_free stays
near-zero (relative to C_small) across thresholds, the bridge is robust;
if it flips, it was a threshold artifact.

Run:  py -3.12 diag_n3.py          # full
      py -3.12 diag_n3.py --test   # quick N=16 sanity
Output: diag_n3_results.json
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

THRESHOLDS=[0.3,0.4,0.5,0.6,0.7]

def measure(uk):
    g=gradu(uk)
    e=0.5*(g+g.transpose(0,1))
    em=e.permute(2,3,4,0,1).reshape(-1,3,3)
    ws=[]
    for i in range(0, em.shape[0], 500_000):
        ws.append(torch.linalg.eigvalsh(em[i:i+500_000]))
    w = torch.cat(ws, dim=0)
    l1,l2,l3=w[:,2],w[:,1],w[:,0]
    denom=(l1**2+l2**2+l3**2)**1.5+1e-12
    s=-3*np.sqrt(6)*(l1*l2*l3)/denom
    om=torch.stack([g[2,1]-g[1,2],g[0,2]-g[2,0],g[1,0]-g[0,1]])
    omf=om.permute(1,2,3,0).reshape(-1,3)
    tr_e3=torch.einsum('pij,pjk,pki->p',em,em,em)
    wew=torch.einsum('pi,pij,pj->p',omf,em,omf)
    Pi=-tr_e3-0.25*wew
    out={}
    for thr in THRESHOLDS:
        free=torch.abs(s)<thr
        small=(l1>1.6*torch.abs(l3))&(~free)
        large=(~free)&(~small)
        def m(mask): return float(Pi[mask].mean()) if mask.sum()>10 else None
        def f(mask): return float(mask.float().mean())
        out[f"{thr}"]=dict(
            free_flux=m(free), small_flux=m(small), large_flux=m(large),
            free_frac=f(free), small_frac=f(small), large_frac=f(large))
    out['flux_full']=float(Pi.mean())
    return out

def main():
    uk=init_field(); t0=time.time()
    print(f"device={device} N={N} thresholds={THRESHOLDS}")
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
    # aggregate per threshold
    agg={}
    for thr in THRESHOLDS:
        key=f"{thr}"
        def avg(field):
            vals=[s[key][field] for s in samples if s[key][field] is not None]
            return float(np.mean(vals)) if vals else None
        agg[key]=dict(
            free_flux=avg('free_flux'), small_flux=avg('small_flux'),
            large_flux=avg('large_flux'), free_frac=avg('free_frac'),
            small_frac=avg('small_frac'), large_frac=avg('large_frac'))
    out=dict(N=N, n_samples=len(samples), thresholds=THRESHOLDS,
             flux_full=float(np.mean([s['flux_full'] for s in samples])),
             per_threshold=agg)
    json.dump(out,open('diag_n3_results.json','w'),indent=2)
    print("\n=== ROBUSTNESS SUMMARY (flux per class vs threshold) ===")
    print(f"{'thr':>5} {'free_flux':>12} {'small_flux':>12} {'large_flux':>12} {'free_frac':>10}")
    for thr in THRESHOLDS:
        a=agg[f"{thr}"]
        ff=a['free_flux']; sf=a['small_flux']; lf=a['large_flux']; fr=a['free_frac']
        print(f"{thr:>5} {ff if ff else 0:>12.2e} {sf if sf else 0:>12.2e} {lf if lf else 0:>12.2e} {fr if fr else 0:>10.3f}")
    print("\nRobust if free_flux stays << small_flux across ALL thresholds.")
    print("Saved diag_n3_results.json — send it back.")

if __name__=='__main__':
    if TESTONLY: print("SELF-TEST N=16"); main(); print("self-test done")
    else: main()
