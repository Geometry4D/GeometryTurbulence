# Geometric Theory of Singularities in 3D Navier–Stokes

A research program on the regularity theory and potential finite-time singularities of the three-dimensional incompressible Navier–Stokes equations, approached through the geometry of the strain-rate tensor.

---

## Overview

The program studies the partial regularity of suitable weak solutions to the 3D Navier–Stokes equations by classifying spatio-temporal regions according to the local structure of the strain-rate tensor **e** = ½(∇u + ∇uᵀ). Three geometric classes are introduced — strong axial stretching (`C_small`), moderate anisotropy with shear (`C_free`, the *free zones*), and large-scale dominated (`C_large`) — and their dynamics are used to derive conditional regularity criteria and bounds on the Hausdorff dimension of the singular set.

The work is organized along two complementary lines:

- **GeometryT** — the geometric mechanism, lower bounds, and conditional blow-up / regularity criteria.
- **Upperbonds** — quantitative conditional upper bounds on the Hausdorff dimension dim_H(E) of the singular set via the screening *Strength* of free zones.

## Status

This is an **active research program, not a body of proven theorems.** The repository records the current mathematical state honestly, distinguishing closed results from conditional ones and from open problems.

| Result | Statement | Status |
|---|---|---|
| **Mode A** | Geometric refinement of the *covering constant* in the Caffarelli–Kohn–Nirenberg theorem via screening Strength | Provable in principle; **central open step: the sign in the geometric vortex-stretching inequality** (see `theory/open_problem_sign.md`) |
| **Mode B** (ER-v2) | dim_H(E) < 1 under self-similar screening + transversality | Conditional; rests on a solid core (random-matrix decorrelation, Frostman) with open links tied to open problems in turbulence |

The classical Caffarelli–Kohn–Nirenberg theorem (1982) gives dim_H(E) ≤ 1. Mode A refines the *constant* in the covering argument; Mode B is a conditional route toward dim_H(E) < 1.

## Repository structure

```
program/    Program overview and roadmap
theory/     Mathematical core — one topic per file (definitions, lemmas, open problems)
article/    Working draft of the Mode A paper
docs/        Navigation and development log
```

Heavy mathematics and technical derivations live in `theory/`, one self-contained file per result. The development history (iteration-by-iteration) is recorded separately in `docs/iteration_log.md`.

## Key references

- L. Caffarelli, R. Kohn, L. Nirenberg, *Partial regularity of suitable weak solutions of the Navier–Stokes equations*, Comm. Pure Appl. Math. 35 (1982), 771–831.
- P. Constantin, C. Fefferman, *Direction of vorticity and the problem of global regularity for the Navier–Stokes equations*, Indiana Univ. Math. J. 42 (1993), 775–789.
- K. Falconer, *The Geometry of Fractal Sets*, Cambridge University Press (Frostman / mass distribution principle).
- R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, J. Fluid Mech. 1 (1956), 497–504.

## Conventions

- Strain-rate tensor **e** = ½(∇u + ∇uᵀ); vorticity **ω** = ∇×u; both with tr **e** = 0 (incompressibility).
- Characteristic length of a region U: L_U = |U|^{1/3}.
- Commit messages follow `[YYYY-MM-DD | iter N] [prefix] description`, prefixes `[prog] [thy] [art] [scr]`.
