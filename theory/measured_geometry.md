# Measured Geometry of Strain Classes in Navier–Stokes

**Status: a coherent, DNS-measured structural picture. A transition structure and a persistence hierarchy that are robust in ordering; one honestly negative result (intermittency is not a class effect at the accessible resolution); and one bridge result (per-class energy flux) that — on closeout audit — is qualitatively real but quantitatively overstated, partially built into the classifier, and not novel against the literature. See the Closeout audit boxes below.**

This collects what local DNS (N = 128, single GPU) measured directly about the strain-class geometry, both Eulerian (per-class diagnostics over a stationary window) and Lagrangian (class dynamics along tracer trajectories). Everything here passed a two-sided check; the negative result is recorded with equal weight. The closeout audit (June 22) revised the strength of the flux result downward; the original §1 is retained with the correction attached, so the record shows both what was measured and how it was re-assessed.

---

## 1. Energy flux per class — free zones are low-flux zones (qualitative; overstated as first written)

The energy-flux density $\Pi = -\mathrm{tr}(e^3) - \tfrac14\,\omega\cdot e\cdot\omega$ (Eyink; Borue–Orszag; the gradient-level / Johnson 2020–21 decomposition), averaged per class on the NS field:

| class | mean flux $\Pi$ | role |
|---|---|---|
| C_small | $-1.7\times10^{-5}$ | sink (forward cascade) |
| C_free | $-4.7\times10^{-7}$ | **buffer (≈ zero, sign not determined)** |
| C_large | $+7.3\times10^{-6}$ | source |

C_free carries flux small in magnitude relative to C_small. The qualitative ordering — C_small a sink, C_large a source, C_free a near-zero buffer — is stable between the N = 16 sanity run and the full N = 128 run.

> **Closeout audit (2026-06-22) — this result is qualitatively real but was overstated. Three corrections:**
>
> 1. **The "36×" figure is not robust.** It is the small/free ratio at the single threshold |s| < 0.5. Across thresholds (`diag_n3_results.json`, thr ∈ {0.3…0.7}) the ratio runs ~16× to unbounded, and **free_flux changes sign at thr = 0.7** (−0.47×10⁻⁶ → +0.44×10⁻⁶). Only "free_flux is 1.5–2 orders of magnitude below small_flux, sign-indefinite near zero" is robust. The fixed "36×" should not be cited.
> 2. **The classifier partially builds the result in.** Free is defined by the shape parameter |s| < thr, and s ∝ λ₁λ₂λ₃/|e|³ — i.e. s is essentially a function of tr(e³), which is one of the two terms of Π. On random traceless tensors corr(|s|, |tr e³|) ≈ 0.46 and corr(s, Π_SSA) ≈ 0.72. So "C_free ≈ 0 flux" is in part a definitional consequence of selecting small |s| (hence small tr(e³)), not purely an independent measurement. A flux study with an honest (flux-decoupled) classifier — e.g. the vorticity–strain ratio r = |ω|²/(2|e|²) — was designed but is not pursued (see §closeout note in the roadmap): the Lagrangian flux-vs-geometry question it would address is already covered by Chevillard–Meneveau (2008) and the Lagrangian RSH literature.
> 3. **The framework is not novel.** Π = −tr(e³) − ¼ω·e·ω is the standard gradient-level decomposition (Borue–Orszag; Eyink; Johnson 2020–21). Class- / topology-conditioned cascade — including "high-strain regions carry forward transfer, vorticity-dominated regions carry suppressed/inverse transfer" — is established (Johnson 2021 on Q–R-conditioned cascade; Nature Sci. Rep. 2024 on the coherent structure of the cascade, ≈85% SSA / <15% VS). This §1 is therefore a **restatement of a known decomposition in the strain-class language — a bridge, not a new result** about anomalous dissipation, and the bridge is on a weakly turbulent N=128 field (urms ≈ 0.004), not the inertial-range regime where the Onsager question lives.

## 2. Lagrangian class dynamics — persistence hierarchy and transition structure (robust)

Tracking ~$10^4$–$2\times10^4$ passive tracers along trajectories and recording the strain class at each particle:

- **Persistence hierarchy (robust):** C_free is the longest-lived class, C_small the shortest-lived and rarest (occupancy ≈ 4 %). This ordering is stable across very different integration horizons, even as absolute lifetimes drift with the (non-stationary) field. Free zones are the persistent skeleton of the flow; strong stretching is a rare, short-lived event.
- **Transition structure (robust):** direct C_small ↔ C_free transitions are essentially absent; transitions between them pass through C_large. Stable across all runs.
- **Quantitative parameters are NOT reliable:** per-class drift, noise, and absolute lifetimes drift monotonically over long runs because the forced field slowly relaxes (the capped forcing does not hold a true steady state over $10^5$ steps). Only the *ordering* and *connectivity* are robust; the numbers are not. Methodological lesson: use short stationary windows or ensembles, not single long runs.

> **Closeout audit (2026-06-22):** the persistence/lifetime hierarchy and transition structure are robust as ordering, but **not novel**: lifetimes and evolution of strain-tensor flow topology are characterized by Elsinga & Marusic (2010, "Evolution and lifetimes of flow topology"), and complex-network treatments of velocity-gradient-tensor transitions exist (PRF 2025). Recorded as a reproduced structural fact, not a new result.

## 3. Intermittency is not a class effect at this resolution (negative)

Flatness of $|\nabla u|$ per class (Gaussian = 3):

| | C_small | C_free | C_large | full |
|---|---|---|---|---|
| flatness | 2.70 | 3.30 | 3.22 | 3.27 |

The full-field flatness (3.27) is only marginally super-Gaussian, and **C_small — the strong-stretching class — is sub-Gaussian (2.70), i.e. the most regular class, not the bursty one** (a single dominant stretching direction gives a structured gradient). An apparent signal in the N = 16 sanity run (C_small flatness 3.95) did **not** survive at N = 128 and is attributed to negligible statistics there. Conclusion: at the accessible Reynolds number there is no class-resolved intermittency picture, and C_small is not its carrier. Developed intermittency would require N > 256, beyond the available 4 GB. This, together with the earlier finding that the three-state model reproduces intermittency only under parameter heterogeneity not present in the measured flow, **closes the intermittency line** within the current means.

## 4. Vorticity–strain alignment — not developed (neutral)

$|\cos\angle(\omega,e_i)|$ per class is ≈ 0.5 for all axes and all classes; the Ashurst intermediate-axis alignment ($\omega \to e_2$) is not visible at this resolution. Neutral, resolution-limited.

## 5. Scale dependence (supporting)

Per-octave class fractions are stable across the two resolved octaves (C_small ≈ 4 %, C_free ≈ 50 %, C_large ≈ 46 %); the smallest octave is a spectral-truncation artifact and is discarded. This supports premise (i) of the conditional dimension result (free zones present with a positive, roughly scale-independent fraction).

---

## The coherent picture

The reliable measurements assemble into one internally consistent structural statement about Navier–Stokes turbulence at this resolution:

> Free zones (C_free) form a persistent, volume-dominant (~50 %) skeleton of the flow that carries comparatively little energy flux; strong stretching (C_small) occupies rare (~4 %), short-lived sink regions; transitions between the two are routed through an intermediate class; and eigenvector orientation decorrelates across scales (E\|cos\| ≈ 0.44–0.49, separate DNS).

This is a measured geometric description, not a theorem about regularity and not a mechanism for intermittency — both of those lines are closed. On closeout audit (June 22) its components were each matched to prior literature (flux decomposition: Borue–Orszag / Eyink / Johnson; topology-conditioned cascade: Johnson 2021, Nature Sci. Rep. 2024; lifetimes/topology: Elsinga–Marusic 2010; strain-class taxonomy: Chong–Perry–Cantwell 1990), and the flux result was found qualitatively correct but quantitatively overstated and partially tautological (§1 box). The value of this file is therefore a **coherent, internally consistent, honestly-audited structural account** of where energy flux lives, which regions persist, and how they connect — restated in the strain-class language — **not a novel measurement**. See `../PROGRAM_CLOSEOUT.md` for the program-level conclusion.
