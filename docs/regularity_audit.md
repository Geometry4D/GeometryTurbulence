# Complete Audit of Regularity Approaches

A systematic record of every known class of approach to the 3D Navier–Stokes regularity problem, the result of attacking it within this program's geometric framework, and the single barrier that unifies the negative outcomes. This document exists so that the closure of the regularity line is demonstrably *thorough*, not premature.

Each entry was tested with two-sided skepticism: every refutation was itself checked for the opposite conclusion before being recorded.

---

## 1. Energy / critical-space methods

| Approach | Result in this framework |
|---|---|
| Ladyzhenskaya–Prodi–Serrin ($L^p_t L^q_x$) | Attacked via one-component reduction (§3). Closed by the *statistics ≠ pointwise* barrier. |
| Critical Besov / $BMO^{-1}$ (Koch–Tataru) | Rejected: the critical norm is an a-priori condition on data *amplitude*; $\dim_H(E)$ is an a-posteriori *size* of the singular set. A small singular set does not imply a small norm — different ends of the problem. No sound bridge. |
| Profile decomposition / critical norms | Not productive without new compactness input; abstract, high risk of unfounded steps. |

## 2. Geometric (vorticity-direction) methods

| Approach | Result |
|---|---|
| Constantin–Fefferman ($\xi_\omega$ Lipschitz) | Used positively in Lemma A3 (free zones regular). As a route to global regularity it hits the barrier. |
| Vortex-stretching depletion (Mode A) | **Closed, rigorous negative.** No sign-definite negative term in the stretching, pointwise or averaged (see `open_problem_sign.md`). |
| Geometric measure / dimension of singular set | Conditional result (Mode B): $\dim_H(E) = 1 + \log_2(1-\varphi_{\rm free})$ under two premises tied to open turbulence problems. |

## 3. Structural (vorticity-magnitude) methods

| Approach | Result |
|---|---|
| Beale–Kato–Majda ($\int\|\omega\|_\infty$) | A class-restricted BKM statement reduces to Lemma A3 (E ⊂ C_small) — no new content. |
| One-component (Chae–Choe, Kukavica–Ziane) | Attacked: decorrelation of stretching-axis orientation is statistical; at the single blow-up point the worst case (axis ∥ fixed direction) gives no pointwise control. Closed by *statistics ≠ pointwise*. |
| Helicity | Closed, negative. Helicity is orthogonal to the strain classification (pure shear in C_free has zero helicity) and is itself supercritical — it does not control regularity. |

## 4. Scaling / self-similar

| Approach | Result |
|---|---|
| Leray self-similar exclusion | Already settled in the literature (Nečas–Růžička–Šverák, 1996). |
| Discretely self-similar (DSS) | Rejected here: DSS requires scale self-repetition (cross-scale correlation), which *contradicts* the orientation decorrelation established for the Gaussian model. Proving decorrelation for a genuine NS solution would exclude DSS — but that is exactly what the model ≠ NS barrier forbids. |
| Type I / Type II blow-up classification | Requires quantitative blow-up data (DNS); out of scope. |

## 5. Constructive (blow-up / non-uniqueness)

| Approach | Result |
|---|---|
| Convex integration / non-uniqueness (De Lellis–Székelyhidi, Buckmaster–Vicol) | **Closed, negative — and explanatory.** The classification needs a *smooth* strain field (eigenvalues, classes); convex-integration solutions are non-smooth, so the strain — and hence the free-zone classification — is not defined on them. The two objects are incompatible. This is precisely why a "conditional non-uniqueness via free zones" formulation cannot work. |
| Numerical blow-up scenarios (Hou et al.) | Requires high-resolution DNS; out of scope by construction. |

## 6. Statistical / turbulence

| Approach | Result |
|---|---|
| Multifractal / intermittency | **Positive result.** The reduced three-state model produces anomalous scaling of structure functions; the driver is class heterogeneity (see `reduced_model_intermittency.md`). |
| Anomalous dissipation (Onsager) | **A genuine bridge, not a breakthrough.** The energy flux $\Pi \sim -\mathrm{tr}(e^3) - \tfrac14\,\omega\cdot e\cdot\omega$ is exactly the program's terms; decomposed by class, C_small carries strong forward cascade while **C_free carries ≈ zero flux** — free zones are zones of suppressed energy flux. This restates known results (Eyink; Borue–Orszag) in the framework's language; it connects the geometry to anomalous dissipation but proves nothing new about dissipation itself. |
| Reduced / shell models | Covered by the three-state model (§6, positive). |

## 7. Conditional criteria (the program's own focus)

| Approach | Result |
|---|---|
| Conditional $\dim_H(E) < 1$ (Mode B) | Conditional theorem; implication provable (~85%), premises open and tied to K41 / turbulence structure. |
| Critical free-zone fraction → regularity | Closed: the naive $(1-\gamma\varphi_{\rm free})$ multiplier fails under enstrophy concentration in C_small; $\gamma$ is not a constant and can vanish at blow-up. |

---

## The single barrier

Every negative outcome above reduces to one barrier, appearing in three equivalent guises:

1. **Nonlocality of pressure** — the pressure Hessian couples regions nonlocally; no local geometric quantity controls it (this closed both Mode A routes and the attempt to derive the reduced model from NS).
2. **Statistics ≠ pointwise** — the framework's controls (orientation decorrelation, class fractions) are ensemble/statistical, while regularity demands control at the single potential singular point.
3. **Model ≠ NS** — the sharp results (orientation decorrelation) are proven for a Gaussian model; transferring them to genuine NS solutions runs into the non-Gaussianity of turbulence.

These are not three separate obstacles but three faces of the same gap between a local/statistical geometric description and the pointwise, nonlocal, fully nonlinear nature of the regularity problem.

## Conclusion

The regularity problem has been attacked from every known class of approach. The geometric framework is **exhausted for regularity** — demonstrably, by a unifying barrier, not by lack of effort. What the program retains as genuine output: a verified technical core (Lemma ODE-1, Lemma A3, Frostman dimension formula, the isotropy/decorrelation result with corrected coefficients), a rigorously closed negative result (Mode A), a conditional result with precisely delineated premises (Mode B), one positive result (three-state intermittency), and one bridge (geometry ↔ anomalous dissipation). The productive direction that does not require DNS is the intermittency branch.
