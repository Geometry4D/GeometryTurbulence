# Roadmap and Status

**Last updated:** 2026-06-22 (program closeout). **STATUS: CLOSED — see [`../PROGRAM_CLOSEOUT.md`](../PROGRAM_CLOSEOUT.md).** The analytic regularity program is exhausted (Mode A refuted; nine angles closed on a single pressure-nonlocality barrier; Mode B unrealizable at natural constants). The empirical results survive two-sided skepticism in ordering but reproduce existing literature; the energy-flux bridge is qualitatively real but quantitatively overstated and partially built into the classifier (corrected below and in `../theory/measured_geometry.md`). The sections below are retained as the development record; the closeout section at the end gives the final state.

## Honest status of the proof chain for dim_H(E) < 1 (Mode B)

| # | Link | Status | Type |
|---|---|---|---|
| 1 | E ⊂ C_small (singularities lie outside free zones) — Lemma A3 | ~85% | two independent proofs |
| 2,3 | CKN ε-regularity; dim_H(E) ≤ 1 | classical | theorem |
| 4 | free zones separate C_small (Cantor mechanism) | reduces to 5 + 6,7 + 10 | mechanism |
| 5 | self-similar cascade (free zones present at all scales) | ~55–60%; **φ_free≈0.5, roughly scale-independent on resolved octaves (DNS, N=128)** | model; supported by DNS, still tied to open K41 |
| 6,7 | transversality (non-nested gaps across scales) | ~50% | requires DNS; class formulation under revision |
| 8,9 | decorrelation of eigenvector orientation, E\|cos\| ≈ ½ | ~70% skeleton; **confirmed on a real NS field by DNS** (E\|cos\|=0.44–0.49, N=128), see `../theory/dns_validation.md` | core, now NS-validated |
| 10 | Frostman: gaps ⟹ dimension formula | ~90% | standard geometric measure theory |

**Resulting formula** (under transversality): dim_H(E) = 1 + log₂(1 − φ_free), where φ_free is the volume fraction of free zones per scale.

The product of confidences across the chain is small: **Mode B is a well-supported conditional conjecture, not a proven theorem.** Its core (random-matrix decorrelation + Frostman + Lemma A3) is solid; the open links (5, 6, 7) are tied to open problems in turbulence theory, not to gaps in the present arguments.

> **Closeout (2026-06-22):** Mode B is now recorded as **closed / unrealizable at natural constants**, not as a live conditional conjecture. Iteration 7 (sensitivity in C₀, C₁), re-verified at closeout, requires ζ(β) < 0.347 at the natural choice C₀ = C₁ = 1, φ = 0.5 — but ζ(β) ≥ 1 always. Mode B can hold only under C₀·C₁ < 0.347 (very strong relaxed-transversality with very weak nesting), which is not justified. This is a clean negative result with a precise unrealizability diagnostic. The verified pieces underneath (Lemma ODE-1; Frostman; Lemma A3 ~85%; the GOE/isotropic-covariance decorrelation, with the corrected non-GOE coefficients) remain correct as standalone mathematics; they are simply not enough to deliver dim_H < 1.

## Status of Mode A (closed — rigorous negative result)

- Text of the draft is essentially complete (`article/mode_A_CKN_constant.md`), but the **mathematical core is now refuted**, rigorously and with two-sided skepticism (see [`../theory/open_problem_sign.md`](../theory/open_problem_sign.md)).
- The deterministic Mode A claim required a sign-definite negative screening term in free zones. It is shown that **no such term exists**: not in vortex stretching (the proposed oscillation is an artifact of inconsistent dynamics; the eigenvalues are real), and not in the pressure term (sign-indefinite pointwise, with explicit counterexamples both ways; and the ensemble average changes sign with Reynolds number).
- This is recorded as a **closed negative result** — a checkable statement that has been settled (refuted). The draft is retained as the record of the approach; it is not submittable as formulated.
- A strictly weaker, regime-conditional statement (a Reynolds-range observation) remains conceivable but is not a screening theorem and is not pursued.

## Positive result: reduced model generates intermittency (2026-06-16)

A minimal three-state stochastic model built from the strain classes (C_small stretching / C_free screening / C_large diffusion, with C_free as transitional hub) reproduces **anomalous scaling of structure functions** — concave $\zeta_p$, multifractal intermittency that K41 does not give. Verified: robust across randomized parameters (100% concave), statistically significant vs single-state ($p=0.0002$), and the anomaly vanishes without class structure (control $\approx 0$, the K41 value). See `../theory/reduced_model_intermittency.md`. This is a reduced model (sufficiency, not derivation from NS), and is the most publishable positive direction in the program (a minimal geometric generator of intermittency).

> **Closeout (2026-06-22):** retained as a *sufficiency* demonstration only. The later Lagrangian DNS (D1) showed the measured flow does **not** carry the parameter heterogeneity the model needs, and the direct class-resolved data show no intermittency (flatness §3 of measured_geometry). So the model shows classes *can* generate intermittency, not that they *do* in NS. Honest standing: a phenomenological generator, not a result about NS.

## Narrowed scope after DNS measurements (2026-06-17)

Direct local DNS (N=128) settled several questions and narrows the program to what is measurable and what survives. See `../theory/measured_geometry.md`.

**Measured, robust (ordering only; see closeout for novelty):**
- **Energy-flux bridge:** C_free carries comparatively little energy flux; C_small is a sink, C_large a source. *(Closeout: the "36× smaller" figure is a single-threshold artifact — free_flux changes sign at thr=0.7 — and the classifier partially builds the result in, since |s| ∝ tr(e³) is one term of Π. Qualitatively real, quantitatively overstated, not novel: Borue–Orszag / Eyink / Johnson / Nature Sci. Rep. 2024. See measured_geometry §1 box.)*
- **Persistence hierarchy + transition structure (Lagrangian):** C_free longest-lived, C_small rarest/shortest-lived; C_small<->C_free transitions routed through C_large. Robust ordering (absolute parameters drift and are not claimed). *(Closeout: reproduces Elsinga–Marusic 2010.)*
- **phi_free ≈ 0.50, roughly scale-independent** on resolved octaves — supports Mode B premise (i).
- **Orientation decorrelation on NS** (E|cos| ≈ 0.44-0.49, earlier DNS). *(Closeout: reproduces the Ashurst/Elsinga line; real on NS but known.)*

**Closed (negative):**
- **Intermittency as a class effect:** full-field flatness only 3.27, and C_small is sub-Gaussian (2.70) — not the bursty class. No class-resolved intermittency at accessible Re; would need N>256. Together with the reduced-model finding (intermittency needs parameter heterogeneity absent in the measured flow), the intermittency line is closed.
- Vorticity-strain alignment: not developed at this resolution (neutral).

The program is thus a **measured geometric description of NS turbulence** (where flux lives, which regions persist, how they connect) — now closed, with every component matched to prior literature. Not a regularity proof, not an intermittency mechanism — both closed.

## Priorities

> **Closeout (2026-06-22): the priorities below are SUPERSEDED.** The program is closed. They are retained only as the record of the last-live plan. No further analytic re-attack; no further GPU runs. See `../PROGRAM_CLOSEOUT.md`.

1. ~~**Mode B — sharpen the conditional result.**~~ Superseded: Mode B closed as unrealizable at natural constants (see Mode B closeout box above).
2. ~~**Close Lemma A3 (85% → 95%).**~~ Superseded: A3 retained at ~85% as correct standalone PDE; not pursued further (the program it served is closed).
3. ~~**Align the free-zone definition** between draft and program.~~ Superseded; recorded as a known naming inconsistency in the retained draft.
4. ~~**Links 5, 6, 7.**~~ Superseded: tied to open turbulence problems; not re-attacked.

## A Lagrangian flux angle was evaluated and not pursued (2026-06-22 closeout)

Before closing, one remaining angle was worked up: a Lagrangian **flux budget per class** with a flux-decoupled classifier (vorticity–strain ratio r = |ω|²/(2|e|²), chosen because on random tensors corr(r, Π) ≈ 0, unlike the shape parameter which is ~tautological with Π). A design note and a tautology-gate (measure corr(r,Π) on the real field *before* trusting any per-class flux) were prepared (`docs/D2_lagrangian_flux_design.md`). It was **not run**: a literature check showed the core measurement — energy flux / enstrophy production conditioned on velocity-gradient geometry *along Lagrangian trajectories* — is already published (Chevillard–Meneveau 2008; Lagrangian Refined Similarity Hypothesis, Benzi et al. 2009; Johnson–Meneveau Annual Review 2024), at Reynolds numbers (Re_λ ~ 400, 2048³) far beyond the available 4 GB. The only arguably-open variant (flux *event-aligned* on discrete class transitions) is narrow, likely a repackaging of the existing continuous Q–R conditional averages, and would almost certainly fail the tautology gate on a real field (vorticity–strain alignment, Ashurst 1987, recouples r to Π dynamically). Recorded as **closed by literature (K4)** rather than run — burning days of compute to reproduce known results on weaker hardware is exactly what the program's rules forbid.

## Closed negative results (recorded to avoid revisiting)

- **Cone / distortion covering** for lowering dim_H: ruled out — Hausdorff dimension is invariant under the diffeomorphic flow map.
- **"Any φ_free > 0 ⟹ dim < 1"**: false — an artifact of ignoring nesting of gaps across scales; corrected to the transversality condition.
- **Degenerate classifiers**: the anisotropy ratio max|λ|/Σ|λ| ≡ ½ for traceless tensors, and the Lund–Rogers shape parameter ≡ 0 on Gaussian random-phase fields. Class structure of strain can therefore only be validated on genuine DNS data, not on synthetic fields.
- **Mode A** (deterministic screening / negative sign): refuted two-sided, with counterexamples (above).
- **Mode B** (dim_H < 1): unrealizable at natural constants — ζ(β) < 0.347 required but ζ(β) ≥ 1 (above).
- **Nine regularity angles** (Mode A stretching, Mode A pressure, BKM-narrowing, critical fraction, single component, derivation-from-NS, helicity, TRIZ-13, cones): all fail on one barrier — class geometry gives ensemble control, regularity needs pointwise control at the singular point. See `docs/regularity_audit.md`.
- **Lagrangian flux-per-class** (this file, above): closed by literature, not run.
