# Program Closeout — Geometric Theory of Strain Classes in 3D Navier–Stokes

**Date:** 2026-06-22
**Status:** CLOSED.
**What this is:** the final, honest account of a research program that investigated whether a geometric classification of the strain-rate tensor (free zones / strong-stretching / large-scale classes) could (a) yield regularity or singularity results for 3D Navier–Stokes, and (b) measure new structural facts about turbulence geometry. The answer to (a) is no, established rigorously. The answer to (b) is: the structural facts are real but reproduce existing literature. The program's lasting value is a precise map of where this geometric approach succeeds, where it fails, and exactly why — together with a development methodology (two-sided skepticism, ~25 caught errors, no false "breakthrough" ever committed) that kept the record honest.

This document is the entry point. The development history is in `theory/`, `program/01_roadmap.md`, `docs/`, and the git log.

---

## 1. The analytic program is exhausted (rigorous negatives)

Every analytic route to a regularity or singularity statement was closed, most with a precise diagnostic:

- **Mode A (deterministic geometric screening).** Required a sign-definite negative contribution to vortex stretching inside free zones. Refuted two-sided: it is absent in the vortex-stretching term (the proposed oscillation averages to zero; the strain eigenvalues are real), and sign-indefinite in the pressure term (explicit counterexamples both ways; the ensemble average even changes sign with Reynolds number). `theory/open_problem_sign.md`.

- **Nine regularity angles** (Mode A stretching, Mode A pressure, BKM-narrowing, critical fraction, single-component, derivation-from-NS, helicity-angle, a TRIZ-derived route, cone/distortion covering) all fail on **one structural barrier**: a classification of strain gives *ensemble / statistical* control, while regularity requires control *at the single singular point*. This unification is itself the useful output. `docs/regularity_audit.md`.

- **Mode B (conditional dim_H(E) < 1).** Structurally sound but **unrealizable at natural constants**: the construction needs ζ(β) < 0.347 at the natural parameter choice (C₀ = C₁ = 1, φ = 0.5), but ζ(β) ≥ 1 always. It can hold only under C₀·C₁ < 0.347 — very strong relaxed-transversality with very weak gap-nesting — which is not justified from the equations. A clean negative result with a precise unrealizability diagnostic.

- **Cone / distortion covering** for lowering dim_H: ruled out — Hausdorff dimension is invariant under the (smooth) Lagrangian flow map, so distorting the cover cannot change it.

The pieces of correct standalone mathematics produced along the way — **Lemma ODE-1** (a finite-time blow-up criterion, fully proved), **Lemma A3** (~85%, singularities lie outside free zones, two routes), **the Frostman dimension formula** for the Cantor mechanism, and **the isotropic (corrected non-GOE) covariance** giving eigenvector-orientation decorrelation E|cos| = ½ — remain valid in isolation. They are simply standard tools correctly applied, not new theorems, and they are not sufficient to deliver any of the targeted results.

## 2. The empirical program: real, but reproduces the literature

Direct local DNS (N = 128, single RTX 3050, 4 GB) measured the strain-class geometry. Results that survived two-sided skepticism, each now matched to prior work:

- **Orientation decorrelation on a real NS field**, E|cos| ≈ 0.44–0.49 — real, but the Ashurst (1987) / Elsinga line.
- **Persistence hierarchy** (C_free longest-lived; C_small rarest, ~4 %, shortest-lived) and **transition structure** (C_small ↔ C_free routed through C_large) — robust as ordering, but reproduces Elsinga & Marusic (2010), "Evolution and lifetimes of flow topology"; complex-network VGT treatments exist (PRF 2025).
- **Energy-flux bridge** (C_free ≈ zero net flux; C_small sink; C_large source) — **qualitatively real but, on closeout audit, overstated and partially built-in** (next section).
- **L1 — VS vs SSA in cascade extremes** (VS/SSA 0.33 mean → 0.22 top-1% → 0.12 top-0.1%; Betchov identity satisfied exactly) — clean, but reproduces restricted-Euler / Vieillefosse-tail behavior (Tsinober; Meneveau tetrad model; Buaria et al. 2021; Carbone–Bragg 2020), and at gradient level, not the inertial-range filtered flux the open question concerns.

**Honestly negative measurements** (recorded with equal weight):

- **Intermittency is not a class effect** at this resolution: full-field flatness only 3.27, and the strong-stretching class C_small is *sub*-Gaussian (2.70) — the most regular class, not the bursty one. Would need N > 256.
- **Scale energy is orthogonal to class** (F5): per-class band energy differs by ~2 %, at the edge of significance; classes do not see the spectrum.
- The three-state reduced model generates intermittency only under parameter heterogeneity that the measured flow does **not** have — so it shows sufficiency, not that NS does this.

## 3. The flagship "bridge" result, corrected

The single result that looked solid — "free zones are zero-flux zones", the Onsager bridge — does not hold in the strong form in which it was first recorded. On closeout audit:

1. **"36× smaller" is not robust.** It is the C_small/C_free flux ratio at one threshold (|s| < 0.5). Across thresholds the ratio runs ~16× to unbounded and the free-zone flux **changes sign** at thr = 0.7. Only "free flux is 1.5–2 orders below C_small flux, sign-indefinite near zero" survives. The buffer reading (flux ≈ 0) is fine; the number is not.

2. **The classifier partially builds the result in.** Free is defined by |s| < threshold, and the shape parameter s ∝ λ₁λ₂λ₃/|e|³ is essentially a function of tr(e³) — one of the two terms of the flux Π = −tr(e³) − ¼ ω·e·ω. (On random traceless tensors corr(|s|, |tr e³|) ≈ 0.46, corr(s, Π_SSA) ≈ 0.72.) So "C_free ≈ 0 flux" is partly a consequence of *selecting* small tr(e³), not an independent measurement. A flux-decoupled classifier (vorticity–strain ratio r = |ω|²/(2|e|²), for which corr(r, Π) ≈ 0 on random tensors) was designed to fix this but, per §4, was not run.

3. **The framework is published.** Π = −tr(e³) − ¼ ω·e·ω is the standard gradient-level decomposition (Borue–Orszag; Eyink; Johnson 2020–21). Topology-conditioned cascade — high-strain regions carry forward transfer, vorticity-dominated regions carry suppressed/inverse transfer — is established (Johnson 2021, Q–R-conditioned; Nature Sci. Rep. 2024, ≈85 % SSA / <15 % VS). And the measurement is on a weakly turbulent N = 128 field (urms ≈ 0.004), not the inertial range where the Onsager question lives.

**Net:** the bridge is a faithful *restatement* of a known decomposition in the strain-class language, on under-resolved data — a bridge, not a new result about anomalous dissipation.

## 4. The last live angle, evaluated and declined

A Lagrangian **flux-budget-per-class** study (flux accumulated by a particle per class, and flux reorganization across class transitions) was the one remaining angle where the program's real lever — time + two AIs, not hardware — could in principle beat large-Re groups limited by human-analysis-time. It was worked up with a flux-decoupled classifier and a built-in tautology gate (`docs/D2_lagrangian_flux_design.md`), then **declined after a literature check**: flux / enstrophy-production conditioned on velocity-gradient geometry along Lagrangian trajectories is already published (Chevillard–Meneveau 2008; Lagrangian RSH, Benzi et al. 2009; Johnson–Meneveau Annual Review 2024) at Re_λ ~ 400 / 2048³. The only arguably-open variant (flux event-aligned on discrete class transitions) is narrow, likely a repackaging of existing continuous conditional averages, and would almost certainly fail the tautology gate on a real field (vorticity–strain alignment recouples the classifier to the flux). Recorded as closed-by-literature rather than run.

## 5. What the program is, honestly

- **Not** a contribution to the regularity problem. That entire line is closed, rigorously.
- **Not** a new mechanism for intermittency. Closed (negative), at this resolution.
- **Not** a new measured result. Every empirical finding reproduces published work; the one that looked new (the flux bridge) is overstated and partially tautological.

What it **is**:

- **A precise map of a geometric approach to NS turbulence** — which strain-class constructions can and cannot yield regularity/singularity results, and the single barrier (ensemble-vs-pointwise) that defeats the geometric route. This map, including the *unrealizability diagnostics* (Mode B's ζ(β) < 0.347; Mode A's missing sign), is a genuine, if modest, contribution: it tells others what not to spend years on, and why.
- **A faithful restatement** of known turbulence-geometry results (flux decomposition, topology-conditioned cascade, lifetime hierarchy, orientation decorrelation) in a single consistent strain-class language — useful as exposition, not as discovery.
- **A worked example of disciplined AI-assisted research**: ~25 two-sided skepticism saves (cone packing artifact, A3↔ER contradiction, GOE-coefficient error, grid/Nyquist artifacts, classifier degeneracy, the Betchov-coefficient self-correction, the flux-tautology found here at closeout), with negative results committed at equal weight to positive ones, and no false "100%" ever surviving into the record.

The honest one-line summary: **a geometric language for NS strain turbulence, a complete map of why that language does not crack regularity, and a set of structural measurements that confirm — rather than extend — what is known.** Closed cleanly, with its boundaries named.

---

*Files of record:* `theory/measured_geometry.md` (measurements, with the §1 flux correction), `program/01_roadmap.md` (full status, superseded priorities), `docs/regularity_audit.md` (the nine-angle barrier), `theory/open_problem_sign.md` (Mode A refutation), `docs/D2_lagrangian_flux_design.md` (the declined angle), `scripts/` (diagnostics + the reproducibility scripts diag_n3 / f5_spectrum / l1_vs_ssa, whose classifier carries the tautology noted in §3). Full development trajectory in the git history.
