# Program Overview

**Geometric Theory of Singularities in 3D Navier–Stokes**

## Goal

Develop a unified geometric theory of regularity and singularity formation for the 3D incompressible Navier–Stokes equations, based on the local structure of the strain-rate tensor. The aim is a coherent series of results combining a geometric mechanism, lower bounds (conditional blow-up / non-uniqueness criteria), and upper bounds on the dimension of the singular set.

## Central object: geometric classification of strain

At each point (x,t) the strain-rate tensor **e**(x,t) is symmetric and traceless. Its eigenvalue structure defines three classes:

- **C_small** — strong axial stretching (one dominant positive eigenvalue). Singularities, if any, live here: this is where vortex stretching can amplify without bound.
- **C_free** (*free zones*) — moderate anisotropy together with a substantial shear component. These regions **screen**: shear rotates the vorticity direction and suppresses persistent alignment with the stretching axis.
- **C_large** — large-scale-dominated, near-isotropic strain.

The precise definitions are in [`../theory/definitions.md`](../theory/definitions.md).

## Two complementary lines

### GeometryT — mechanism and lower bounds
A conditional geometric blow-up criterion in the regime of small geometric complexity, built from:
- geometric complexity `C_geo(U)` and geometric flux `J_geo(U,t)`,
- a geometric vortex-stretching inequality (Constantin–Fefferman–Majda spirit),
- a closed ODE blow-up lemma (fully proven, see [`../theory/lemma_ODE1_blowup.md`](../theory/lemma_ODE1_blowup.md)).

### Upperbonds — conditional upper bounds on dim_H(E)
Quantitative conditional bounds on the Hausdorff dimension of the singular set via the screening *Strength* of free zones. The route to dim_H(E) < 1 (Mode B) rests on:
- a Cantor / mass-distribution mechanism (free zones cut the singular set into gaps),
- a random-matrix decorrelation theorem for the orientation of strain eigenvectors across scales (see [`../theory/GOE_decorrelation.md`](../theory/GOE_decorrelation.md)),
- the Frostman mass distribution principle (see [`../theory/frostman_dimension.md`](../theory/frostman_dimension.md)).

## Three regimes of result

| Regime | Statement | Conditions | Honest status |
|---|---|---|---|
| **A** | refinement of the *constant* in CKN covering | none beyond suitable weak solution + positive screening | provable in principle; open step is the sign in the vortex-stretching inequality |
| **B** (ER-v2) | dim_H(E) < 1 | self-similar screening + transversality of free-zone gaps | conditional; solid core, open links tied to open turbulence problems |
| **C** | dim_H(E) < 1 via cone/distortion covering | — | **closed (dead end):** dim_H is invariant under the (diffeomorphic) flow map, so distortion covering cannot lower it |

Regime C is recorded as a closed negative result: it was ruled out on topological grounds (Hausdorff dimension is bi-Lipschitz / diffeomorphism invariant), which redirected the program toward the spatial-gap (Cantor) mechanism of Mode B.

## Methodology

The program develops iteratively. Each iteration ends with either a closed lemma/theorem or an explicitly labelled sketch carrying an honest assessment of rigor. Numerical experiments are used throughout to falsify candidate mechanisms before they are promoted to claims; several candidate results were discarded this way (see `docs/iteration_log.md`).
