"""
D1: Lagrangian calibration of the three-state strain-class model from DNS.

Advects ~10^4 passive tracer particles in a forced-isotropic-turbulence DNS
(N=128, GPU) and measures ALONG trajectories:
  - class of each particle (C_small / C_free / C_large) from local strain
  - transition matrix P_ij between classes
  - mean lifetime of each class
  - drift a_k = <d ln|grad u|/dt> within class k
  - noise sigma_k within class k

ITERATIVE / BACKGROUND USE:
  Writes accumulated statistics to d1_progress.json every CHECKPOINT steps,
  with error bars and the number of transitions sampled. You watch that file
  as an external control loop: stop when P, a, sigma have converged (small
  error bars) — not on a timer. Re-run appends nothing; just restart for more.

Run:  py -3.12 d1_lagrangian.py          # full
      py -3.12 d1_lagrangian.py --test   # quick N=16 sanity
"""
import torch, numpy as np, json, time, sys

TESTONLY = '--test' in sys.argv
device = 'cuda' if torch.cuda.is_available() else 'cpu'
dtype, ctype = torch.float32, torch.complex64

# ---------------- config ----------------
N        = 16 if TESTONLY else 128
nu       = 0.02 if TESTONLY else 0.006
dt       = 0.01 if TESTONLY else 0.0015
n_part   = 200 if TESTONLY else 20000
force_k  = 2
force_eps= 0.12
warmup   = 40 if TESTONLY else 3000        # let turbulence develop before tracking
CHECKPOINT = 20 if TESTONLY else 500       # write progress every this many steps
n_steps  = 120 if TESTONLY else 200000     # upper bound; stop by convergence (you)
torch.manual_seed(0)

# ---------------- spectral operators ----------------
k1 = torch.fft.fftfreq(N, d=1.0/N).to(device)
KX,KY,KZ = torch.meshgrid(k1,k1,k1, indexing='ij')
K2 = KX**2+KY**2+KZ**2; K2c = K2.clone(); K2c[0,0,0]=1.0
Kmag = torch.sqrt(K2); kmax=N//3
dealias = ((torch.abs(KX)<=kmax)&(torch.abs(KY)<=kmax)&(torch.abs(KZ)<=kmax)).to(dtype)
Kl=[KX,KY,KZ]

def project(uk):
    div=KX*uk[0]+KY*uk[1]+KZ*uk[2]
    return torch.stack([uk[0]-KX*div/K2c, uk[1]-KY*div/K2c, uk[2]-KZ*div/K2c])

def init_field():
    a=torch.randn(3,N,N,N,dtype=dtype,device=device)
    ak=torch.fft.fftn(a,dim=(1,2,3)).to(ctype)
    env=(Kmag**2)*torch.exp(-(Kmag/4.0)**2); env=env/(env.max()+1e-12)
    return project(ak*env)

def nonlinear(uk):
    u=torch.fft.ifftn(uk,dim=(1,2,3)).real
    ok=torch.stack([1j*(KY*uk[2]-KZ*uk[1]),1j*(KZ*uk[0]-KX*uk[2]),1j*(KX*uk[1]-KY*uk[0])])
    om=torch.fft.ifftn(ok,dim=(1,2,3)).real
    c=torch.stack([u[1]*om[2]-u[2]*om[1], u[2]*om[0]-u[0]*om[2], u[0]*om[1]-u[1]*om[0]])
    ck=torch.fft.fftn(c,dim=(1,2,3)).to(ctype)*dealias
    return project(ck)

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

# ---------------- velocity & strain in physical space ----------------
def velocity(uk):
    return torch.fft.ifftn(uk,dim=(1,2,3)).real           # (3,N,N,N)

def gradu_field(uk):
    g=torch.empty(3,3,N,N,N,device=device,dtype=dtype)
    for i in range(3):
        for j in range(3):
            g[i,j]=torch.fft.ifftn(1j*Kl[j]*uk[i],dim=(0,1,2)).real  # d u_i / d x_j
    return g

# ---------------- trilinear interpolation at particle positions ----------------
def interp(field, pos):
    # field: (...,N,N,N) ; pos: (P,3) in [0,N) periodic. Returns (...,P)
    P=pos.shape[0]
    x=pos%N
    x0=torch.floor(x).long(); x1=(x0+1)%N
    w1=x-x0.float(); w0=1.0-w1
    xb=x0%N
    ix0,iy0,iz0=xb[:,0],xb[:,1],xb[:,2]
    ix1,iy1,iz1=x1[:,0],x1[:,1],x1[:,2]
    wx0,wy0,wz0=w0[:,0],w0[:,1],w0[:,2]
    wx1,wy1,wz1=w1[:,0],w1[:,1],w1[:,2]
    def gather(fz):
        # fz: (...,N,N,N) -> (...,P) at the 8 corners, trilinear
        f=fz
        c000=f[...,ix0,iy0,iz0]; c100=f[...,ix1,iy0,iz0]
        c010=f[...,ix0,iy1,iz0]; c110=f[...,ix1,iy1,iz0]
        c001=f[...,ix0,iy0,iz1]; c101=f[...,ix1,iy0,iz1]
        c011=f[...,ix0,iy1,iz1]; c111=f[...,ix1,iy1,iz1]
        return (c000*wx0*wy0*wz0 + c100*wx1*wy0*wz0 +
                c010*wx0*wy1*wz0 + c110*wx1*wy1*wz0 +
                c001*wx0*wy0*wz1 + c101*wx1*wy0*wz1 +
                c011*wx0*wy1*wz1 + c111*wx1*wy1*wz1)
    return gather(field)

# ---------------- classify particles from local strain ----------------
def classify(g_at):
    # g_at: (3,3,P) grad u at particles -> strain eigenvalues -> class id
    P=g_at.shape[-1]
    e=0.5*(g_at+g_at.transpose(0,1))            # (3,3,P) symmetric strain
    em=e.permute(2,0,1)                          # (P,3,3)
    w=torch.linalg.eigvalsh(em)                  # ascending (P,3)
    l1,l2,l3=w[:,2],w[:,1],w[:,0]                # l1>=l2>=l3
    denom=(l1**2+l2**2+l3**2)**1.5+1e-12
    s=-3*np.sqrt(6)*(l1*l2*l3)/denom             # shape param in [-1,1]
    maxabs=torch.maximum(torch.abs(l1),torch.abs(l3))
    # class ids: 0=small(stretch,l1 dominant), 1=free(shear,|s| small), 2=large
    cls=torch.full((P,),2,device=device,dtype=torch.long)   # default large
    free=(torch.abs(s)<0.5)
    small=(l1> 1.6*torch.abs(l3))&(~free)        # strong axial stretching
    cls[free]=1; cls[small]=0
    gradnorm=torch.linalg.matrix_norm(em)        # |grad u|-ish per particle
    return cls, gradnorm

# ---------------- accumulators ----------------
trans=torch.zeros(3,3,dtype=torch.float64)       # transition counts
occ=torch.zeros(3,dtype=torch.float64)           # occupancy counts
dlog_sum=torch.zeros(3,dtype=torch.float64)      # sum of d ln|gradu| within class
dlog_sq =torch.zeros(3,dtype=torch.float64)      # sum of squares
dlog_cnt=torch.zeros(3,dtype=torch.float64)
run_len=torch.zeros(3,dtype=torch.float64)       # sum of run lengths (lifetime)
run_num=torch.zeros(3,dtype=torch.float64)       # number of runs

def write_progress(it, t0):
    P=trans.sum(dim=1,keepdim=True); Pmat=(trans/(P+1e-12))
    a=(dlog_sum/(dlog_cnt+1e-12))/dt                       # drift per unit time
    var=(dlog_sq/(dlog_cnt+1e-12))-(dlog_sum/(dlog_cnt+1e-12))**2
    sig=torch.sqrt(torch.clamp(var,min=0))/np.sqrt(dt)
    life=(run_len/(run_num+1e-12))*dt
    ntr=float(trans.sum())
    a_err=(sig/torch.sqrt(dlog_cnt+1e-12)).tolist()        # SE of drift
    out=dict(step=it, n_transitions=ntr, elapsed_s=time.time()-t0,
             transition_matrix=Pmat.tolist(),
             occupancy_fraction=(occ/(occ.sum()+1e-12)).tolist(),
             drift_per_class=a.tolist(), drift_SE=a_err,
             noise_per_class=sig.tolist(),
             lifetime_per_class=life.tolist(),
             class_order=["C_small","C_free","C_large"])
    json.dump(out, open('d1_progress.json','w'), indent=2)
    print(f"  ckpt step {it}: transitions={ntr:.0f}  occ={np.round((occ/(occ.sum()+1e-12)).tolist(),3)}"
          f"  drift={np.round(a.tolist(),3)}  life={np.round(life.tolist(),3)}")

# ---------------- main ----------------
def main():
    uk=init_field(); t0=time.time()
    print(f"device={device} N={N} particles={n_part}  warmup={warmup} steps")
    for it in range(warmup):
        uk=step(uk)
        if it%max(1,warmup//4)==0:
            E=float((velocity(uk)**2).sum().real)*0.5/N**3
            print(f"  warmup {it}/{warmup} E={E:.3e}")
            if not np.isfinite(E): print("  blow-up in warmup"); return
    # seed particles uniformly
    pos=torch.rand(n_part,3,device=device)*N
    g=gradu_field(uk); g_at=interp(g,pos); prev_cls,prev_gn=classify(g_at)
    prev_log=torch.log(prev_gn+1e-12)
    print("tracking...")
    for it in range(n_steps):
        uk=step(uk)
        u=velocity(uk)
        # advect particles: x += u(x)*dt  (RK1 is fine at small dt)
        u_at=interp(u,pos).transpose(0,1)         # (P,3)
        pos=(pos+u_at*dt)%N
        g=gradu_field(uk); g_at=interp(g,pos)
        cls,gn=classify(g_at); logn=torch.log(gn+1e-12)
        # accumulate transitions & occupancy
        for i in range(3):
            occ[i]+=float((cls==i).sum())
        idx=prev_cls*3+cls
        tc=torch.bincount(idx,minlength=9).reshape(3,3).double().cpu()
        trans+=tc
        # drift/noise of ln|gradu| within the (previous) class
        dlogn=(logn-prev_log)
        for i in range(3):
            m=(prev_cls==i)
            if m.any():
                d=dlogn[m].double().cpu()
                dlog_sum[i]+=float(d.sum()); dlog_sq[i]+=float((d**2).sum()); dlog_cnt[i]+=float(d.numel())
        # lifetime: count run continuations vs switches
        same=(cls==prev_cls)
        for i in range(3):
            cont=float(((prev_cls==i)&same).sum()); sw=float(((prev_cls==i)&(~same)).sum())
            run_len[i]+=cont+sw; run_num[i]+=sw
        prev_cls,prev_log=cls,logn
        if not torch.isfinite(u).all(): print("  non-finite field, stopping"); break
        if it%CHECKPOINT==0 and it>0:
            write_progress(it,t0)
    write_progress(n_steps,t0)
    print("done. d1_progress.json holds the calibrated parameters.")

if __name__=='__main__':
    if TESTONLY:
        print("SELF-TEST N=16"); main(); print("self-test OK")
    else:
        main()
