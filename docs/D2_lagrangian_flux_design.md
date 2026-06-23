# D2 — Lagrangian Flux Budget per Strain-Class (design doc)

**Date:** 22 June 2026
**Status:** design, pre-GPU. One testable claim, explicit kill-conditions.
**Frame:** final paper = (1) systematized strain-class language + (2) ONE clean
measured result + (3) full audit of method limits. This is the candidate for (2).

---

## 0. Why this angle (the only live one)

Analytic branch closed (Mode A refuted; regularity dead on 9 angles; Mode B
unrealizable at natural constants). Empirical statics reproduce literature
(orientation decorrelation = Elsinga-Marusic 2010; lifetime = same; Onsager
bridge = Borue-Orszag/Johnson + Nature SciRep 2024, and overstated + partially
tautological). The ONLY lever left is time + two AIs on **Lagrangian** statistics
that big-Re groups under-explore for lack of human-analysis-time — NOT a measurement
that needs their Re.

---

## 1. The one claim to test

> Along Lagrangian trajectories in forced isotropic turbulence, the **energy-flux
> budget a fluid particle accumulates depends on the geometric class it resides in**,
> and the flux **reorganizes systematically across a class transition** — in particular
> across the entry/exit of a shear-dominated (free) episode.

Operationally: measure, per particle, time-resolved
  Pi(t) = -tr(e^3) - (1/4) omega.e.omega   along the trajectory,
binned by **residence class** and **aligned to transition events**.

Output quantities:
- `flux_budget[class]` = mean of Pi conditioned on current class (per unit time)
- `dwell[class]` = residence-time distribution per class (we already have ordering)
- `Pi_around_transition[type][lag]` = Pi averaged in a window ±L steps around each
  class-change event, by transition type (e.g. strain->free, free->vortex)

---

## 2. Classifier — vorticity-strain ratio (kills the tautology)

OLD axis: shape param s ∝ l1*l2*l3 / |e|^3. CHECK on random tensors:
  corr(|s|, |tr e^3|) = +0.46 ; corr(s, Pi_SSA) = +0.72   -> classifying by |s|
  pre-selects the flux numerator. THIS is why "C_free ≈ 0 flux" was built-in.

NEW axis: r(x) = |omega|^2 / (2 |e|^2).  CHECK on random tensors:
  corr(r, Pi_SSA)=0.000, corr(r, Pi_VS)=0.001, corr(r, Pi_full)=0.001
  -> r is ~orthogonal to flux on isotropic ensemble. Classifying by r => measuring
  flux-vs-geometry becomes a real measurement, not a definitional consequence.

Class definition (3 bands on r, calibrated to terciles of the r-PDF, NOT hardcoded):
  r < r_lo            -> strain-dominated   (was ~C_small)
  r_lo <= r <= r_hi   -> mixed/shear        (was ~C_free, the "free zone")
  r > r_hi            -> vorticity-dominated (was ~C_large)
Keep the C_small/C_free/C_large NAMES (preserves our language for paper §systematize),
but the AXIS is now r, decoupled from Pi.

---

## 3. GATE (run FIRST, before trusting any flux number)

On the real NS field (not random tensors), measure:
  G = corr(r(x), Pi(x))   over all grid points, in the stationary window.

- |G| < ~0.15  -> classifier is honest on NS; proceed to flux budget.
- |G| >= ~0.15 -> vorticity-strain ALIGNMENT (Ashurst 1987) has re-coupled r to Pi
  through dynamics; the tautology is back via correlation. STOP, do not report flux;
  either (a) switch axis to Q-R quadrant, or (b) report only dwell-time results.

This gate is the whole discipline: we do NOT assume r is neutral on NS just because
it was neutral on random tensors. We measure it.

---

## 4. Field must be turbulent (not the laminar-ish current run)

Current dns: urms=0.0038, zeta_3=2.84 (mixed dissipative/inertial). For Lagrangian
transport to be meaningful, particles must actually survive class changes during a
correlation time.
- forcing: keep the CAPPED scheme (uncapped constant-power NaN'd at step 3000 in chat
  — do NOT revert that), but raise target eps so urms -> O(0.2-0.5).
- CFL guard on dt at higher urms (else blow-up, not turbulence).
- report Lagrangian correlation time T_L vs class dwell times: need dwell ~ a few * dt
  and T_L resolvable, else transitions are noise.

---

## 5. Stationarity by ensemble, not by length (lesson from D1)

D1 fact: 200k-step run DRIFTED off stationarity (occupancy 0.49->0.80, drifts /3).
So: ensemble of M independent SHORT windows (~3000-8000 steps), different forcing-phase
seed per window. Accumulate statistics across ensemble. Checkpoint to JSON every K steps.
You watch convergence of error bars (external control loop) — stop on convergence, not timer.

Robust-by-design (survived D1 skepticism): dwell-time ORDERING (free longest).
Discard-by-design (D1 artifacts): absolute drift, drift ordering, occupancy.

---

## 6. Novelty boundary (honest, pre-emptive)

- Lifetime/persistence alone: NOT novel (Elsinga-Marusic 2010). We do not claim it.
- Transition network alone: NOT novel (complex-network VGT, PRF 2025).
- Q-R Lagrangian evolution: Johnson-Meneveau (Annual Rev 2024) — adjacent.
- CANDIDATE novelty: **flux budget conditioned on a vorticity-strain class AND aligned
  to class-transition events** — flux reorganization across a shear episode, on
  Lagrangian trajectories. Not found in the chat's literature scan. LOW confidence it's
  fully new; MUST web-search before claiming. Likely outcome: "careful Lagrangian
  characterization", not "breakthrough". That is fine for output (2).

---

## 7. Kill-conditions (any one => this angle closes, honestly, into the audit)

K1. Gate fails: |G| >= 0.15 on NS and Q-R fallback also couples -> no honest flux axis.
K2. Field won't turbulate within VRAM at usable dt (blow-up vs laminar, no middle) ->
    Lagrangian transport not resolvable.
K3. flux_budget across classes differs by < error bars on the ensemble -> no signal
    (classes don't see the flux; mirrors the F5/U5 intermittency-null).
K4. Web search finds the exact measurement published -> fold into audit as "reproduced",
    do not claim novelty.

If any K fires: this becomes a clean negative entry in the §audit (method boundary),
exactly like Mode A / Mode B. The paper still stands on language + audit; we just don't
get output (2) from here and report the null.

---

## 8. First concrete step (if approved)

Rewrite d1_lagrangian.py ->  d2_flux_lagrangian.py:
  - classifier on r (terciles, calibrated per-window)
  - GATE computation G=corr(r,Pi) printed FIRST each window
  - per-class flux budget + transition-aligned Pi windows
  - capped forcing with raised eps + CFL guard
  - ensemble of short windows, JSON checkpoint per K steps (your control loop)
Then: --test at N=16 (seconds), then full N=128 via Claude Code CLI on your GPU.
