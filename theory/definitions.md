# Definitions

Mathematical core of the program. All objects below are used consistently throughout `theory/`.

**Standing notation.** u is the velocity field, p the pressure, ω = ∇×u the vorticity. The strain-rate tensor is **e** = ½(∇u + ∇uᵀ), symmetric with tr **e** = 0 by incompressibility. For a bounded region U ⊂ ℝ³, L_U = |U|^{1/3} is its characteristic length. Angle brackets ⟨·⟩_U denote the average over U.

---

## 1. Geometric complexity of a region

For a bounded region U ⊂ ℝ³,

$$
C_{\mathrm{geo}}(U) := \frac{1}{|U|}\int_U \left( |\nabla \mathbf{e}|^2 + \frac{|\mathbf{e} - \overline{\mathbf{e}}_U|^2}{L_U^2} \right) dx,
\qquad \overline{\mathbf{e}}_U = \frac{1}{|U|}\int_U \mathbf{e}\,dx .
$$

It measures both the magnitude of strain gradients and the spatial inhomogeneity of the strain inside U.

---

## 2. Geometric flux (primary form)

Pointwise density:
$$
j_{\mathrm{geo}}(x,t) := \mathbf{e}:\nabla\mathbf{e} + \tfrac12\,\boldsymbol{\omega}\cdot(\nabla\times\mathbf{e}).
$$

Integral geometric flux:
$$
J_{\mathrm{geo}}(U,t) := \int_U j_{\mathrm{geo}}(x,t)\,dx + B(U,t),
$$
where B(U,t) is the boundary flux through ∂U.

**Convention on B(U,t).** For periodic domains, or when the vorticity support is compactly contained in U, set B(U,t) = 0. In general |B(U,t)| ≤ C ‖**e**‖_{L²(∂U)} ‖∇**e**‖_{L²(∂U)}; a full control of this term is deferred (see roadmap, open issues).

**Naming convention.** Throughout, J_geo without a superscript denotes this primary form. The vorticity-stretching form below is always written with the superscript "vort".

---

## 2′. Vorticity-stretching flux (derived quantity)

$$
J^{\mathrm{vort}}_{\mathrm{geo}}(U,t) := \int_U \big(\boldsymbol{\omega}\cdot\mathbf{e}\cdot\boldsymbol{\omega}\big)\,dx + R(U,t).
$$

This is the direct vortex-stretching quantity entering the energy / enstrophy identity. It is related to the primary form through the geometric vortex-stretching inequality (see `geometric_vortex_stretching.md`): at the integral level,
$$
J^{\mathrm{vort}}_{\mathrm{geo}}(U,t) \gtrsim c\,L_U\,J_{\mathrm{geo}}(U,t)\,\frac{\|\boldsymbol{\omega}\|_{L^2(U)}^2}{\langle|\mathbf{e}|\rangle_U\,|U|} - (\text{error via } C_{\mathrm{geo}}),
$$
with remainder |R(U,t)| ≤ C C_geo(U) (‖∇u‖²_{L²(U)} + ‖∇u‖³_{L³(U)}).

---

## 3. Screening Strength

$$
\mathrm{Strength}(U(t)) := \int_{\text{free zones}(t)} \big( |e_{zz}(x,t)| + |e_{r\theta}(x,t)| \big)\,dx,
$$
with the working relation Strength(U) ≍ |J_geo(U)| / ⟨|**e**|⟩_U.

**Note.** This form mixes physical dimensions and must be normalized by characteristic scales (U₀, L₀, T₀) before use in a dimensionally consistent estimate. An invariant reformulation through the eigenvalues of **e** is in progress.

---

## 4. Effective spectral width

$$
\Delta\alpha_{\mathrm{eff}} := \frac{\Delta\alpha_{\mathrm{outside}}}{1 + |J_{\mathrm{geo}}|/L_{\mathrm{free}}},
$$
where Δα_outside is the multifractal spectral width contributed by regions outside the free zones.

---

## 5. Characteristic size of free zones

$$
L_{\mathrm{free}}(t) := \frac{\displaystyle\int_{\text{free zones}(t)} \sigma(x,t)\,d(x,t)\,dx}{\displaystyle\int_{\text{free zones}(t)} \sigma(x,t)\,dx},
\qquad \sigma(x,t) = |e_{zz}| + |e_{r\theta}|,
$$
the Strength-weighted mean linear size of free zones, where d(x,t) is the local distance to the zone boundary.

---

## 6. Auxiliary function for the transition-measure estimate

$$
g(x) = C\,\frac{x}{1+x},
$$
monotone, bounded above (g → C as x → ∞), g(0)=0; used in the alternative bound dim_H(E) ≤ 1 + g(∫₀ᵀ |T(t)|^α dt).

---

## Geometric classes

The classification is stated in cylindrical components (r,θ,z) adapted to the local stretching axis; e_zz is the axial component, e_rθ the principal shear component.

### C_small — strong axial stretching
**e**(x,t) ∈ C_small near x at scale λ if
- |e_zz| ≥ c₁ max_{ij}|e_{ij}|, with c₁ ≥ 1.6,
- |e_rθ| ≥ c₂ |e_zz|, with c₂ ≥ 0.45,
- |e_rr + e_θθ| ≤ c₃ |e_zz|, with c₃ ≤ 0.45,
- significant small-scale content (via Littlewood–Paley projection).

This is the class where finite-time singularities, if they occur, are located.

### C_large — large-scale dominated
**e**(x,t) ∈ C_large if
- max_{ij}|e_{ij}| ≤ c₁ (⅑ Σ|e_{ij}|), with c₁ ≤ 1.4,
- large-scale contributions dominate.

### C_free — free zone (screening region)
**e**(x,t) ∈ C_free if
- c₁ max|e_{ij}| ≤ |e_zz| ≤ c₂ max|e_{ij}|, with 0.25 ≤ c₁ ≤ 0.35 and 0.65 ≤ c₂ ≤ 0.75 (moderate anisotropy),
- |e_rr + e_θθ| ≤ c₃ |e_zz|, with c₃ ≤ 0.65,
- |e_rθ| ≥ c₄ (⅑ Σ|e_{ij}|), with c₄ ≥ 0.35 (substantial shear),
- small energy content at scale λ: E(λ) ≤ δ ‖**e**‖²_{L²}, δ ≪ 1.

The role of C_free is to **screen**: the substantial shear component continuously and smoothly rotates the vorticity, preventing persistent alignment with the stretching axis. This is the geometric content of Lemma A3.

> **Consistency note.** In the Mode A paper draft the "free zone" is defined by *strong* axial stretching (e₁₁ ≥ (1−δ)|**e**|), which is the C_small regime here, not C_free. This naming conflict must be resolved (see roadmap, priority 3).

### Active two-sided cascade
Near a time T a two-sided cascade is active if there are sequences t_k, s_k, r_k → T with regions on which the strain transitions into C_small (forward branch, growth of μ_small), into C_large (backward branch), and into C_free as transitional states with small energy content.
