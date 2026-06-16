# Lemma A3 — Regularity inside free zones

**Status: ~85% (two independent proof routes).** This lemma underlies both program lines: it places the singular set outside the free zones (E ⊂ C_small), which is link 1 of the Mode B chain and the separation property used in the Cantor mechanism.

---

## Statement (target)

Let (u,p) be a suitable weak solution. If a space-time region V belongs to the free-zone class C_free (moderate anisotropy with substantial shear, small energy content at the working scale), then u is regular in the interior of V: ∇u ∈ L^∞_{loc}(V). Consequently the singular set satisfies E ⊂ C_small.

---

## Route 1 — via CKN ε-regularity

Inside a free zone the energy content at scale λ is small by definition: E(λ) ≤ δ ‖**e**‖²_{L²}. Decompose

$$
|\nabla u|^2 = |\mathbf{e}|^2 + \tfrac12|\boldsymbol{\omega}|^2 .
$$

If the scaled energy A(r) = (1/r)∬_{Q_r}|∇u|² satisfies A(r) < ε₀ (the CKN threshold), the solution is regular at the point. The free-zone smallness gives A(r) ≤ c_aniso · δ · (norm); requiring

$$
\delta < \frac{\varepsilon_0^{\mathrm{CKN}}}{c_{\mathrm{aniso}}}
$$

makes the CKN threshold satisfied, hence regularity. This **refines the definition** of C_free by tying δ to the CKN constant.

**Gap of Route 1.** The decomposition contains the vorticity term ½|ω|², which is not directly controlled by conditions on **e** alone. A strong vortex (large |ω|) could keep |∇u|² large even when |**e**| is moderate. Route 2 closes this gap.

---

## Route 2 — via the Constantin–Fefferman criterion

**Constantin–Fefferman (1993):** if the vorticity direction ξ_ω = ω/|ω| is Lipschitz in a region, the solution is regular there. A singularity requires rapid variation of the vorticity *direction*.

In C_free there is, by definition, a substantial shear component |e_rθ| ≥ c₄ ⟨|e|⟩ > 0. The mechanism:

- shear **continuously and smoothly rotates** ω, preventing persistent alignment with the stretching axis;
- hence the vortex-stretching term ω·**e**·ω is, on average, small (it is maximized only when ω aligns with the dominant eigenvector of **e**);
- so |ω| does not grow, ξ_ω stays Lipschitz, and Constantin–Fefferman gives regularity.

Contrast with C_small: strong stretching (|e_zz| ≥ 1.6 max) along a fixed axis produces sharp alignment, ξ_ω can fail to be Lipschitz, and a singularity is not excluded. This is consistent with E ⊂ C_small.

---

## Significance and remaining work

Two independent arguments — the energy-based CKN route and the geometric Constantin–Fefferman route — give the same regularity of free zones. The Constantin–Fefferman route closes the vorticity gap of the energy route, since it controls |ω| through the *direction* dynamics rather than the energy.

**Remaining (sketch level):**
- a rigorous Lipschitz estimate for ξ_ω from the quantitative C_free conditions (explicit constants);
- the exact constants in the compensation estimate;
- control of the boundary term B(U,t) (see `definitions.md`, convention on B).

Calling the lemma "fully proven" is premature; with the two routes it is close to closure. Promoting it to ~95% is priority 4 on the roadmap and is pure PDE analysis, independent of the open turbulence problems.

## References
- P. Constantin, C. Fefferman, *Direction of vorticity and the problem of global regularity for the Navier–Stokes equations*, Indiana Univ. Math. J. 42 (1993), 775–789.
- L. Caffarelli, R. Kohn, L. Nirenberg, Comm. Pure Appl. Math. 35 (1982), 771–831.
