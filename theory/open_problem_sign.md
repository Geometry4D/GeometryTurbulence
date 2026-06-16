# Open Problem — The Sign in the Geometric Vortex-Stretching Inequality

**Status: OPEN. This is the central unresolved step of Mode A.**

This file isolates the single mathematical question on which the Mode A result (refinement of the CKN covering constant) depends. It is recorded prominently and honestly because text-completeness of the draft does **not** imply this step is closed.

---

## The inequality in question (Lemma 2.4 of the Mode A draft)

In a free zone with Strength S₀, for suitable cut-offs φ, the draft asserts
$$
\int \boldsymbol{\omega}\cdot(\mathbf{e}\,\boldsymbol{\omega})\,\phi^2\,dx
\;\le\; -\,c\,S_0\int |u|^2\,\phi^2\,dx
\;+\; C_{\mathrm{geo}}\int |u|^2|\nabla\phi|^2\,dx
\;+\; C'\int |\nabla u|^2\,\phi^2\,dx .
$$

The **negative leading term** −c S₀ ∫|u|²φ² is the heart of Mode A: fed into the pressure estimate it raises the ε-regularity threshold linearly in S₀, which shrinks the CKN covering constant by a factor ∝ (1 + c S_min).

---

## Why the sign is not obvious

The vortex-stretching density ω·**e**·ω is, in a region of strong axial stretching, typically **positive** — stretching amplifies vorticity. This is the very mechanism that drives potential singularity formation. Asserting an integrated bound ≤ −c S₀ ∫|u|² (negative) requires that the shear component suppress stretching **more** than stretching amplifies vorticity.

That is a genuine inequality between two competing effects, not a normalization. The draft's Appendix A only sketches the absorption ("three steps: integration by parts, extraction of the leading positive term, absorption using shear and the controlled geometric flux"). The decisive sign is asserted, not derived.

---

## Internal conflict to resolve first

The program contains a second inequality for the same quantity with the **opposite** sign — a *lower* bound of the form
$$
\int_U \boldsymbol{\omega}\cdot\mathbf{e}\cdot\boldsymbol{\omega}\,dx \;\gtrsim\; c\,J_{\mathrm{geo}}(U,t) - (\text{error}),
$$
arising on the C_small / blow-up side of the theory (it is what drives the ODE blow-up criterion). One quantity, two inequalities pulling in opposite directions. These must be reconciled — presumably they apply to different classes (C_free vs C_small) under different hypotheses — **before** either is built upon. Clarifying this is a prerequisite, not an afterthought.

---

## Proposed resolution path (falsifiable numerical test first)

The recommended next step is a test designed to be able to **disprove** the inequality, not to confirm it:

1. **Scan a 2D parameter map**: shear strength |e_rθ| (axis 1) × axial stretching |e_zz| (axis 2), from moderate to strong.
2. At each point compute the sign of ∫ ω·**e**·ω.
3. Check whether the region where the sign is **negative** coincides with the C_free definition (moderate anisotropy + strong shear).
4. Use **worst-case vorticity**: take ω aligned with the stretching axis ξ₁, where ω·**e**·ω is maximally positive. If the sign is negative even there, the mechanism is robust; if not, the inequality is false as stated.

Three outcomes, all informative:
- negative sign exactly on C_free → mechanism confirmed, Mode A is close;
- negative sign only elsewhere (e.g. only at extreme shear absent from C_free) → the free-zone definition must be changed to match the physics;
- never negative at physical parameters → Lemma 2.4 is false as stated and Mode A must be rebuilt.

**Caveat on the test.** The sign of ω·**e**·ω depends strongly on the orientation of ω relative to the eigenframe of **e**; ω must not be fixed arbitrarily. Either average over a physical ω distribution or use the worst case above.

---

## Honest assessment

Rigor of this step: **~35%** (a logical schema exists; the decisive sign is unproven). Any status label of "100%" or "closed" for Mode A that ignores this is inflation. Until the sign is established (analytically, or at least mapped and confirmed numerically, and ideally checked by a PDE specialist), Mode A is not a complete proof.
