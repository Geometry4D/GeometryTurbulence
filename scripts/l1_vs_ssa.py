"""
L1: Vortex stretching (VS) vs strain self-amplification (SSA) in the
FLUCTUATIONS of the energy cascade. Tests the open question (Carbone &
Bragg, JFM 2020): VS is sub-leading in the MEAN cascade but may lead in
large FLUCTUATIONS. Pointwise decomposition => Reynolds number not
critical; the leverage is LONG statistics (ensemble of stationary
windows) to resolve tails/extremes.

Definitions (homogeneous turbulence):
  SSA(x) = -tr(S^3) = -S_ij S_jk S_ki
  VS(x)  = (1/4) omega . S . omega
  Betchov identity: <omega.S.omega> = -4 <tr(S^3)>  (mean check)
  flux density Pi ~ SSA + VS

Measured per stationary window, accumulated over an ensemble:
  - Betchov identity (validation that the field is genuine NS)
  - joint stats: corr(SSA,VS), means, ratio SSA:VS (cf 5:3)
  - tails: kurtosis & high quantiles of SSA, VS, Pi
  - conditional <SSA|Pi>q>, <VS|Pi>q> at extreme flux quantiles
    -> which mechanism dominates extreme cascade events?
  - histograms of SSA, VS, Pi (for PDF tails)

Run:  py -3.12 l1_vs_ssa.py            # full N=128 ensemble
      py -3.12 l1_vs_ssa.py --test     # quick N=16 sanity
Output: l1_progress.json (updated every window — watch tails converge).
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
# ensemble: many stationary windows; re-randomize forcing phase between blocks
n_windows=3 if TESTONLY else 60        # leverage: many windows = tail statistics
window_gap=10 if TESTONLY else 200     # steps between sampled windows (decorrelate)
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
def init_field(seed):
    g=torch.Generator(device=device); g.manual_seed(seed)
    a=torch.randn(3,N,N,N,dtype=dtype,device=device,generator=g)
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
    gg=min(max((force_eps/(e+1e-12))**0.5,0.8),1.25)
    f=torch.zeros_like(uk); f[:,shell]=(gg-1.0)*uk[:,shell]; return f
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

# histogram bins (fixed, in units of std, set after first window)
NB=80

def window_stats(uk):
    g=gradu(uk)
    S=0.5*(g+g.transpose(0,1))
    om=torch.stack([g[2,1]-g[1,2],g[0,2]-g[2,0],g[1,0]-g[0,1]])
    # SSA = -tr(S^3), VS = (1/4) w.S.w
    S2=torch.einsum('ijxyz,jkxyz->ikxyz',S,S)
    tr_S3=torch.einsum('ikxyz,kixyz->xyz',S2,S).reshape(-1)
    SSA=(-tr_S3)
    wSw=torch.einsum('ixyz,ijxyz,jxyz->xyz',om,S,om).reshape(-1)
    VS=0.25*wSw
    Pi=SSA+VS
    return SSA, VS, Pi, float(tr_S3.mean()), float(wSw.mean())

def main():
    t0=time.time()
    # accumulators (CPU float64)
    acc=dict(n=0, SSA_sum=0.,VS_sum=0.,SSA2=0.,VS2=0.,SSA3=0.,VS3=0.,SSA4=0.,VS4=0.,
             Pi_sum=0.,Pi2=0.,Pi4=0., SSAVS=0., trS3_sum=0.,wSw_sum=0., nwin=0)
    # conditional on extreme Pi: accumulate SSA,VS for top-1% and top-0.1% |Pi|
    cond=dict(top1_SSA=0.,top1_VS=0.,top1_n=0, top01_SSA=0.,top01_VS=0.,top01_n=0)
    # histograms in std units
    hist_edges=np.linspace(-15,15,NB+1)
    hSSA=np.zeros(NB); hVS=np.zeros(NB); hPi=np.zeros(NB)
    uk=init_field(12345)
    print(f"device={device} N={N} windows={n_windows}")
    for w in range(n_windows):
        # warmup only on first window; then keep evolving with gaps
        steps = warmup if w==0 else window_gap
        for it in range(steps):
            uk=step(uk)
        E=float((torch.fft.ifftn(uk,dim=(1,2,3)).real**2).sum().real)*0.5/N**3
        if not np.isfinite(E):
            print(f"  window {w}: non-finite, reinit"); uk=init_field(1000+w); continue
        SSA,VS,Pi,trS3m,wSwm=window_stats(uk)
        SSA_n=SSA.cpu().numpy().astype(np.float64)
        VS_n=VS.cpu().numpy().astype(np.float64)
        Pi_n=Pi.cpu().numpy().astype(np.float64)
        m=SSA_n.size
        acc['n']+=m; acc['nwin']+=1
        acc['SSA_sum']+=SSA_n.sum(); acc['VS_sum']+=VS_n.sum()
        acc['SSA2']+=(SSA_n**2).sum(); acc['VS2']+=(VS_n**2).sum()
        acc['SSA3']+=(SSA_n**3).sum(); acc['VS3']+=(VS_n**3).sum()
        acc['SSA4']+=(SSA_n**4).sum(); acc['VS4']+=(VS_n**4).sum()
        acc['Pi_sum']+=Pi_n.sum(); acc['Pi2']+=(Pi_n**2).sum(); acc['Pi4']+=(Pi_n**4).sum()
        acc['SSAVS']+=(SSA_n*VS_n).sum()
        acc['trS3_sum']+=trS3m; acc['wSw_sum']+=wSwm
        # conditional on extreme |Pi|
        ap=np.abs(Pi_n); thr1=np.quantile(ap,0.99); thr01=np.quantile(ap,0.999)
        sel1=ap>=thr1; sel01=ap>=thr01
        cond['top1_SSA']+=SSA_n[sel1].sum(); cond['top1_VS']+=VS_n[sel1].sum(); cond['top1_n']+=sel1.sum()
        cond['top01_SSA']+=SSA_n[sel01].sum(); cond['top01_VS']+=VS_n[sel01].sum(); cond['top01_n']+=sel01.sum()
        # histograms in std units (use running std estimate)
        sd_SSA=np.sqrt(acc['SSA2']/acc['n']); sd_VS=np.sqrt(acc['VS2']/acc['n']); sd_Pi=np.sqrt(acc['Pi2']/acc['n'])
        hSSA+=np.histogram(SSA_n/ (sd_SSA+1e-30),bins=hist_edges)[0]
        hVS +=np.histogram(VS_n/(sd_VS+1e-30),bins=hist_edges)[0]
        hPi +=np.histogram(Pi_n/(sd_Pi+1e-30),bins=hist_edges)[0]
        if w%max(1,n_windows//12)==0 or w==n_windows-1:
            n=acc['n']
            mSSA=acc['SSA_sum']/n; mVS=acc['VS_sum']/n
            vSSA=acc['SSA2']/n-mSSA**2; vVS=acc['VS2']/n-mVS**2
            kSSA=(acc['SSA4']/n)/((acc['SSA2']/n)**2+1e-300)
            kVS=(acc['VS4']/n)/((acc['VS2']/n)**2+1e-300)
            corr=(acc['SSAVS']/n-mSSA*mVS)/(np.sqrt(vSSA*vVS)+1e-300)
            betchov=acc['wSw_sum']/(-4*acc['trS3_sum']+1e-300)
            out=dict(window=w, n_points=int(n), elapsed_s=time.time()-t0,
                betchov_ratio=betchov,
                mean_SSA=mSSA, mean_VS=mVS, ratio_SSA_VS=mSSA/(mVS+1e-300),
                kurt_SSA=kSSA, kurt_VS=kVS, corr_SSA_VS=corr,
                cond_top1_meanSSA=cond['top1_SSA']/(cond['top1_n']+1e-9),
                cond_top1_meanVS=cond['top1_VS']/(cond['top1_n']+1e-9),
                cond_top01_meanSSA=cond['top01_SSA']/(cond['top01_n']+1e-9),
                cond_top01_meanVS=cond['top01_VS']/(cond['top01_n']+1e-9),
                hist_edges=hist_edges.tolist(), hist_SSA=hSSA.tolist(),
                hist_VS=hVS.tolist(), hist_Pi=hPi.tolist())
            json.dump(out,open('l1_progress.json','w'),indent=2)
            r1s=cond['top1_SSA']/(cond['top1_n']+1e-9); r1v=cond['top1_VS']/(cond['top1_n']+1e-9)
            print(f"  win {w:3d}: Betchov={betchov:.2f} ratio SSA:VS={mSSA/(mVS+1e-300):.2f} "
                  f"kurt SSA/VS={kSSA:.0f}/{kVS:.0f} | extreme-flux <SSA>/<VS>={r1s:.2e}/{r1v:.2e} "
                  f"(VS/SSA={r1v/(r1s+1e-30):.2f})")
    print("\nDone. l1_progress.json holds joint VS/SSA statistics.")
    print("Key: in extreme-flux events, is VS/SSA ratio > mean ratio? (Carbone-Bragg open Q)")

if __name__=='__main__':
    if TESTONLY: print("SELF-TEST N=16"); main(); print("self-test done")
    else: main()
