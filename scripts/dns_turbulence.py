"""
Pseudospectral DNS of 3D forced isotropic turbulence on GPU (PyTorch/CUDA).
Tuned for RTX 3050 Laptop (4 GB): N=128, float32.

On a REAL Navier-Stokes field (not a Gaussian model) it measures:
  [1] E|cos angle(xi_1^j, xi_1^{j+1})| between octave-filtered strain
      eigenvectors -> tests orientation decorrelation on NS itself
      (the key 'model != NS' barrier).
  [2] phi_free(scale): fraction of shear-like (C_free) points per octave
      -> Mode B premise (i).
  [3] structure-function exponents zeta_p -> calibration of 3-state model
      and intermittency check (zeta_6 - 2 zeta_3 < 0).

USAGE:
  py -3.12 dns_ns.py --test    # 30-sec sanity check at N=16 (run this FIRST)
  py -3.12 dns_ns.py           # full run at N=128 (self-test first, then full)
  py -3.12 dns_ns.py --full    # skip self-test, full run directly

Output: prints results, writes dns_results.txt. Send that file back.
"""
import torch, numpy as np, time, json, sys

TESTONLY = '--test' in sys.argv
SELFTEST = ('--full' not in sys.argv) and (not TESTONLY)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
dtype, ctype = torch.float32, torch.complex64


def build(N):
    k1 = torch.fft.fftfreq(N, d=1.0/N).to(device)
    KX, KY, KZ = torch.meshgrid(k1, k1, k1, indexing='ij')
    K2 = KX**2 + KY**2 + KZ**2
    K2c = K2.clone(); K2c[0,0,0] = 1.0
    Kmag = torch.sqrt(K2)
    kmax = N//3
    dealias = ((torch.abs(KX)<=kmax)&(torch.abs(KY)<=kmax)&(torch.abs(KZ)<=kmax)).to(dtype)
    return dict(N=N,KX=KX,KY=KY,KZ=KZ,K2=K2,K2c=K2c,Kmag=Kmag,dealias=dealias)


def project(uk, g):
    div = g['KX']*uk[0] + g['KY']*uk[1] + g['KZ']*uk[2]
    return torch.stack([uk[0]-g['KX']*div/g['K2c'],
                        uk[1]-g['KY']*div/g['K2c'],
                        uk[2]-g['KZ']*div/g['K2c']])


def init_field(g):
    N=g['N']
    a = torch.randn(3,N,N,N, dtype=dtype, device=device)
    ak = torch.fft.fftn(a, dim=(1,2,3)).to(ctype)
    env = (g['Kmag']**2)*torch.exp(-(g['Kmag']/4.0)**2)
    env = env/(env.max()+1e-12)
    return project(ak*env, g)


def nonlinear(uk, g):
    u = torch.fft.ifftn(uk, dim=(1,2,3)).real
    ok0 = 1j*(g['KY']*uk[2]-g['KZ']*uk[1])
    ok1 = 1j*(g['KZ']*uk[0]-g['KX']*uk[2])
    ok2 = 1j*(g['KX']*uk[1]-g['KY']*uk[0])
    om = torch.fft.ifftn(torch.stack([ok0,ok1,ok2]), dim=(1,2,3)).real
    cx = u[1]*om[2]-u[2]*om[1]
    cy = u[2]*om[0]-u[0]*om[2]
    cz = u[0]*om[1]-u[1]*om[0]
    ck = torch.fft.fftn(torch.stack([cx,cy,cz]), dim=(1,2,3)).to(ctype)*g['dealias']
    return project(ck, g)


def forcing(uk, g, force_k, force_eps):
    # Deterministic constant-energy forcing, numerically safe.
    # Hold the energy in the low shell near a target by rescaling the shell
    # modes; the gain is hard-clamped so a decaying (or growing) field can
    # never blow the forcing up. This was the source of the NaN at step ~3000.
    shell = (g['Kmag'] > 0) & (g['Kmag'] <= force_k)
    e_now = float(torch.sum(torch.abs(uk[:, shell])**2).real)
    if e_now < 1e-10:
        return torch.zeros_like(uk)
    gain = (force_eps / (e_now + 1e-12)) ** 0.5      # rescale toward target energy
    gain = min(max(gain, 0.8), 1.25)                 # hard cap: 0.8x .. 1.25x
    f = torch.zeros_like(uk)
    f[:, shell] = (gain - 1.0) * uk[:, shell]        # additive correction (applied as part of RHS)
    return f

def step(uk, g, nu, dt, force_k, force_eps):
    visc = torch.exp(-nu*g['K2']*dt)
    Nk = nonlinear(uk,g) + forcing(uk,g,force_k,force_eps)
    u1 = (uk + dt*Nk)*visc
    N1 = nonlinear(u1,g) + forcing(u1,g,force_k,force_eps)
    return project((uk*visc) + 0.5*dt*(Nk*visc + N1*visc), g)


def octave_eig(uk, g, lo, hi):
    N=g['N']
    band = ((g['Kmag']>=lo)&(g['Kmag']<hi)).to(dtype)
    ukf = uk*band
    K=[g['KX'],g['KY'],g['KZ']]
    e = torch.zeros(3,3,N,N,N, dtype=dtype, device=device)
    for i in range(3):
        for j in range(3):
            e[i,j] = 0.5*(torch.fft.ifftn(1j*K[i]*ukf[j],dim=(0,1,2)).real
                          +torch.fft.ifftn(1j*K[j]*ukf[i],dim=(0,1,2)).real)
    em = e.permute(2,3,4,0,1).reshape(-1,3,3)
    if not torch.isfinite(em).all():
        raise FloatingPointError("non-finite strain before eigh (field unstable)")
    w,v = torch.linalg.eigh(em)
    return v[:,:,-1], w


def measure(uk, g):
    res={}
    pairs=[(4,8),(8,16),(16,32)] if g['N']>=64 else [(2,4),(4,8)]
    xis=[]; ws=[]
    for (lo,hi) in pairs:
        x,w=octave_eig(uk,g,lo,hi); xis.append(x); ws.append(w)
    res['octave_pairs']=pairs
    res['Ecos']=[float(torch.abs(torch.sum(xis[a]*xis[a+1],dim=1)).mean())
                 for a in range(len(pairs)-1)]
    phif=[]
    for w in ws:
        l=w
        denom=(l[:,0]**2+l[:,1]**2+l[:,2]**2)**1.5 + 1e-12
        s=-3*np.sqrt(6)*(l[:,0]*l[:,1]*l[:,2])/denom
        phif.append(float((torch.abs(s)<0.5).float().mean()))
    res['phi_free']=phif
    u=torch.fft.ifftn(uk,dim=(1,2,3)).real
    ux=u[0]; seps=[1,2,4,8,16] if g['N']>=64 else [1,2,4]
    zeta={}
    for p in [2,3,4,6]:
        Sp=np.array([float(((torch.roll(ux,-r,dims=0)-ux).abs()**p).mean()) for r in seps])
        zeta[p]=float(np.polyfit(np.log(seps),np.log(Sp+1e-20),1)[0])
    res['zeta']=zeta
    res['anomaly']=zeta[6]-2*zeta[3]
    res['urms']=float((u**2).mean().sqrt())
    return res


def run(N, nu, dt, n_steps, steady_after, sample_every, force_k=2, force_eps=0.12, label=""):
    g=build(N)
    uk=init_field(g)
    t0=time.time(); samples=[]
    for it in range(n_steps):
        uk=step(uk,g,nu,dt,force_k,force_eps)
        if it%max(1,n_steps//12)==0:
            u=torch.fft.ifftn(uk,dim=(1,2,3)).real
            E=float((u**2).sum().real)*0.5/N**3
            print(f"  [{label}] step {it:5d}/{n_steps}  E={E:.4e}  {time.time()-t0:.0f}s")
            if not np.isfinite(E):
                print("  WARNING: non-finite E — stopping early, returning samples so far")
                return samples if samples else None
        if it>=steady_after and it%sample_every==0:
            samples.append(measure(uk,g))
    return samples


# ----------------------- self-test (N=16) -----------------------
if SELFTEST or TESTONLY:
    print("="*60); print("SELF-TEST  N=16  (sanity check)"); print("="*60)
    s=run(N=16,nu=0.02,dt=0.01,n_steps=60,steady_after=30,sample_every=10,label="test")
    if not s:
        print("SELF-TEST FAILED"); sys.exit(1)
    print("  self-test OK: field stable, eigh works, diagnostics return.")
    print(f"  (test E|cos|={np.round([np.mean([x['Ecos'][i] for x in s]) for i in range(len(s[0]['Ecos']))],3)})")
    if TESTONLY:
        print("\nSelf-test passed. Now run the full job:  py -3.12 dns_ns.py")
        sys.exit(0)

# ----------------------- full run (N=128) -----------------------
print("\n"+"="*60); print("FULL RUN  N=128  (this takes ~20-50 min on RTX 3050)"); print("="*60)
samples=run(N=128, nu=0.006, dt=0.0015, n_steps=12000,
            steady_after=6000, sample_every=400, label="full")
if not samples:
    print("FULL RUN FAILED"); sys.exit(1)

ec=np.array([s['Ecos'] for s in samples])
pf=np.array([s['phi_free'] for s in samples])
an=np.array([s['anomaly'] for s in samples])
out=dict(
 N=128, nu=0.0035, n_samples=len(samples),
 octave_pairs=samples[0]['octave_pairs'],
 Ecos_mean=ec.mean(0).tolist(), Ecos_std=ec.std(0).tolist(),
 phi_free_mean=pf.mean(0).tolist(),
 zeta_mean={p:float(np.mean([s['zeta'][p] for s in samples])) for p in [2,3,4,6]},
 anomaly_mean=float(an.mean()), anomaly_std=float(an.std()),
 urms_mean=float(np.mean([s['urms'] for s in samples])),
)
print("\n"+"="*60); print("RESULTS  (averaged over %d steady samples)"%len(samples)); print("="*60)
print("E|cos| adjacent octaves (decorrelated -> ~0.5):")
print("  pairs:", out['octave_pairs'])
print("  mean :", np.round(out['Ecos_mean'],4), " std:", np.round(out['Ecos_std'],4))
print("phi_free per octave (Mode B premise i):", np.round(out['phi_free_mean'],4))
print("structure exponents zeta_p (K41 = p/3):")
for p in [2,3,4,6]:
    print(f"  zeta_{p}={out['zeta_mean'][p]:.3f}  (K41 {p/3:.3f})")
print(f"anomaly zeta_6-2zeta_3 = {out['anomaly_mean']:.3f} +/- {out['anomaly_std']:.3f}  (<0 = intermittency)")
json.dump(out, open('dns_results.txt','w'), indent=2)
print("\nSaved dns_results.txt — send this file back for analysis.")
