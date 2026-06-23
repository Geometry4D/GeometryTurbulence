# Geometric Theory of Strain Classes in 3D Navier–Stokes

**STATUS: CLOSED (2026-06-22). See [`PROGRAM_CLOSEOUT.md`](PROGRAM_CLOSEOUT.md) for the full final account.**

A research program that investigated whether a geometric classification of the strain-rate tensor of the 3D incompressible Navier–Stokes equations could yield regularity / singularity results, and whether it could measure new structural facts about turbulence geometry. The program is now closed. This repository is its honest record: what was tried, what was proven, what was refuted, and the single barrier that defeats the geometric route to regularity.

---

## Outcome in one paragraph

The analytic route is **exhausted**, rigorously: the deterministic mechanism (Mode A) is refuted with two-sided skepticism, every known class of regularity approach was tried and closed by a single unifying barrier (a local/statistical geometric description cannot control the pointwise, nonlocal, nonlinear regularity problem), and the conditional dimension result (Mode B) is **unrealizable at natural constants** (it needs ζ(β) < 0.347 while ζ(β) ≥ 1 always). The empirical route produced measurements that are real but **reproduce existing literature**; the one result that initially looked solid — "free zones carry ≈ zero energy flux" — is on audit qualitatively correct but quantitatively overstated and partially built into the classifier. The lasting value is a precise, honestly-audited **map of why this geometric approach does not crack regularity**, plus correct standalone technical lemmas, plus a disciplined development record (~25 two-sided skepticism corrections, no false "breakthrough" committed).

## What the program studied

Spatio-temporal regions were classified by the local structure of the strain-rate tensor **e** = ½(∇u + ∇uᵀ): strong axial stretching (`C_small`), moderate anisotropy with shear (`C_free`, the *free zones*), and large-scale-dominated (`C_large`). The dynamics of these classes were used to attempt conditional regularity criteria and bounds on the Hausdorff dimension of the singular set, and DNS was used to measure the class geometry directly.

## Final status of the two main results

| Result | Statement | Final status |
|---|---|---|
| **Mode A** | Geometric refinement of the covering constant in the Caffarelli–Kohn–Nirenberg theorem via screening Strength | **CLOSED — rigorous negative.** No sign-definite negative screening term exists: not in vortex stretching (eigenvalues real; proposed oscillation was an artifact), not in the pressure term (sign-indefinite pointwise, with explicit counterexamples; ensemble average changes sign with Reynolds number). See [`theory/open_problem_sign.md`](theory/open_problem_sign.md). |
| **Mode B** | dim_H(E) < 1 under self-similar screening + transversality | **CLOSED — unrealizable at natural constants.** Requires ζ(β) < 0.347 at the natural parameter choice, but ζ(β) ≥ 1 always; holds only under C₀·C₁ < 0.347, which is not justified. A clean negative result with a precise unrealizability diagnostic. |

The classical Caffarelli–Kohn–Nirenberg theorem (1982) gives dim_H(E) ≤ 1; neither Mode A nor Mode B improves on it. Both are recorded as settled negative results.

## What is correct and reusable

These are standard tools, correctly applied — valid in isolation, not new theorems, and not sufficient for the targeted results:

- **Lemma ODE-1** — a finite-time blow-up criterion (fully proved). `theory/lemma_ODE1_blowup.md`
- **Lemma A3** — singularities lie outside free zones, ~85%, two independent routes. `theory/lemma_A3_regularity.md`
- **Frostman dimension formula** for the Cantor/gap mechanism. `theory/frostman_dimension.md`
- **Eigenvector-orientation decorrelation** from isotropic covariance (with corrected non-GOE coefficients). `theory/GOE_decorrelation.md`

## What was measured (DNS, N = 128, single GPU)

Real, but reproducing prior work — see [`theory/measured_geometry.md`](theory/measured_geometry.md) for the audited account:

- Orientation decorrelation on a real NS field (E|cos| ≈ 0.44–0.49) — reproduces the Ashurst/Elsinga line.
- Persistence hierarchy and transition structure of strain classes — reproduces Elsinga–Marusic (2010).
- Energy-flux bridge (C_free low flux; C_small sink; C_large source) — qualitatively real but the "36×" figure is a single-threshold artifact, the classifier partially builds the result in (|s| ∝ tr e³ is one term of the flux), and the decomposition is known (Borue–Orszag; Eyink; Johnson 2020–21; Nature Sci. Rep. 2024).
- **Negative:** no class-resolved intermittency at this resolution (C_small is sub-Gaussian, not bursty); scale energy is orthogonal to class.

## Repository structure

```
PROGRAM_CLOSEOUT.md   Final account — start here
program/    Program overview and roadmap (closeout-annotated)
theory/     Mathematical core — one topic per file (definitions, lemmas, refutations)
article/    Working draft of the Mode A paper (retained as record; claim refuted)
docs/        Regularity audit, development log, the declined Lagrangian-flux design note
scripts/    DNS and diagnostics (PyTorch/CUDA) + reproducibility scripts and result JSONs
```

The development history (iteration-by-iteration) is in `docs/iteration_log.md`; the systematic regularity audit and the unifying barrier are in `docs/regularity_audit.md`.

## Key references

- L. Caffarelli, R. Kohn, L. Nirenberg, *Partial regularity of suitable weak solutions of the Navier–Stokes equations*, Comm. Pure Appl. Math. 35 (1982), 771–831.
- P. Constantin, C. Fefferman, *Direction of vorticity and the problem of global regularity for the Navier–Stokes equations*, Indiana Univ. Math. J. 42 (1993), 775–789.
- G. L. Eyink, *Locality of turbulent cascades*, Physica D 207 (2005); V. Borue, S. Orszag, *Local energy flux and subgrid-scale statistics*, J. Fluid Mech. 366 (1998).
- P. L. Johnson, *Energy transfer from large to small scales via vortex stretching and strain self-amplification*, Phys. Rev. Lett. / J. Fluid Mech. (2020–2021).
- G. E. Elsinga, I. Marusic, *Evolution and lifetimes of flow topology in a turbulent boundary layer*, Phys. Fluids 22 (2010).
- R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, J. Fluid Mech. 1 (1956), 497–504.
- K. Falconer, *The Geometry of Fractal Sets*, Cambridge University Press (Frostman / mass distribution principle).

## Conventions

- Strain-rate tensor **e** = ½(∇u + ∇uᵀ); vorticity **ω** = ∇×u; both with tr **e** = 0 (incompressibility).
- Characteristic length of a region U: L_U = |U|^{1/3}.
- The program is closed; commit history records the development. The final commit is the closeout.
