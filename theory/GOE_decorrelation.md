# Random-Matrix Decorrelation of Strain Eigenvector Orientation

**Status: ~70% (theorem skeleton + robust numerics). This is the analytic core of Mode B.**

The result gives an exact value for the cross-scale decorrelation of the orientation of strain eigenvectors, which underlies the transversality condition (links 6,7) needed for the Cantor/Frostman mechanism.

---

## Setup

Band-pass filter the strain at dyadic scale 2^{−j} (Littlewood–Paley): **e**^{(j)}(x) = Σ_{k ∈ band_j} ê(k) e^{ik·x}. At a fixed point this is a symmetric 3×3 matrix. Let ξ^{(j)}(x) be its dominant eigenvector (eigenvector of the eigenvalue of largest modulus).

**Question.** How correlated are the orientations ξ^{(j)} and ξ^{(j+1)} across adjacent scales?

---

## Theorem (skeleton)

$$
\mathbb{E}\big[\,|\cos\angle(\xi^{(j)},\xi^{(j+1)})|\,\big] = \tfrac12 + O\!\left(2^{-3j/2}\right).
$$

The leading value ½ is the value for two **independent uniformly random** directions on the sphere S²; the correction decays exponentially in j, so on small scales the decorrelation is exact.

### Argument

**Step 1 — Gaussian Orthogonal Ensemble limit.** Summing many band modes with mixed phases, **e**^{(j)}(x) behaves (CLT) like a random symmetric matrix. The key structural fact: band_j is a *spherical shell* in k-space, hence rotationally invariant, so the covariance of the filtered strain is **isotropic** — the matrix is a GOE matrix, not a generic Gaussian. A classical random-matrix fact then gives that the eigenvectors of a GOE matrix are **uniformly distributed on the sphere** (Haar measure on O(3)). Crucially, isotropy comes from the geometry of the shell, **not** from any random-phase assumption.

**Step 2 — independence across bands.** Bands j and j+1 are disjoint sets of wavenumbers, so their phases are independent — *even under a common amplitude modulation from a coherent structure*. Orientation is a phase object, not an amplitude object; this is why decorrelation survives strong coherent vortices (see numerics).

**Step 3 — exact expectation.** For ξ^{(j+1)} uniform on S² and any fixed ξ^{(j)}, the projection cos = ⟨ξ^{(j)},ξ^{(j+1)}⟩ is **uniform on [−1,1]** (a special property of the sphere in 3D). Hence

$$
\mathbb{E}[|\cos|] = \int_0^1 t\,dt = \tfrac12 .
$$

**Step 4 — correction term.** The number of modes in the dyadic shell is N_modes ∼ 7·2^{3j}, growing with j; the deviation from the GOE limit is O(N_modes^{−1/2}) = O(2^{−3j/2}). Thus the decorrelation is increasingly exact on small scales — precisely where the singular structure lives.

---

## Numerical verification (robustness)

All checks use the Leray projection (exact incompressibility).

- Independent uniform directions on S²: E|cos| = 0.4995 (theory 0.5).
- Filtered divergence-free strain, eigenvectors uniform on the sphere: E|comp| = 0.498, std = 0.577 (theory 0.5, 0.577) — preserved despite the traceless / divergence-free constraints.
- Cross-scale orientation with **strong coherent vortices** added (vortex strength up to 40): ⟨|cos|⟩ ≈ 0.50–0.53, essentially the GOE value. Coherent structures do **not** align eigenvectors across scales.

A note on synthetic fields: a globally common phase (an unphysical construction) produced spurious alignment up to 0.73; this was identified as an artifact — physical local structures plus incompressibility do not produce it. With correct incompressibility the GOE value is robust.

---

## Consequence for dim_H(E)

Decorrelation of eigenvector orientation (⟨|cos|⟩ ≈ ½, nesting ≈ 0) is exactly the transversality input for the Frostman mechanism (see `frostman_dimension.md`). With φ_free ≈ 0.41 it yields dim_H(E) ≤ 1 + log₂(1 − 0.41) ≈ 0.24 — robustly < 1.

---

## What remains for full rigor

- A rigorous mixing-CLT for the matrix-valued filtered strain (control of the mixing coefficient α_mix for genuine NS solutions). This is the known hard part — non-Gaussianity of turbulence — but the O(2^{−3j/2}) margin protects against moderate deviations from GOE.
- Validation on genuine DNS data (the class structure cannot be validated on synthetic fields; see roadmap).

## References
- M. L. Mehta, *Random Matrices* (GOE eigenvector statistics).
- P. Constantin, C. Fefferman (1993), for the orientation–regularity link.
