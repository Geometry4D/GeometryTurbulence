# The Sign in the Geometric Vortex-Stretching Inequality — CLOSED (refuted)

**STATUS: CLOSED (2026-06-22). This was the central step of Mode A; it is now a rigorous NEGATIVE result. Program closed — see [`../PROGRAM_CLOSEOUT.md`](../PROGRAM_CLOSEOUT.md).**

This file isolates the single mathematical question on which the Mode A result (refinement of the CKN covering constant) depended, and records its resolution: the required sign-definite negative term **does not exist**, neither in vortex stretching nor in the pressure term nor in its ensemble average. Mode A does not hold as formulated. The investigation is preserved in full below — including the original "open" framing and the falsifiable test that closed it — because the *path* to the refutation, with two-sided skepticism at each step, is the point.

> **Reading note.** The sections immediately below were written while the step was still open; they state the question and the test. The two dated updates at the end (both 2026-06-15) carry the rigorous closure. The historical "~35% rigor / OPEN" language is retained verbatim in those early sections as the development record; the final status is CLOSED-negative, as stated in this header and in the closing conclusion.

---

## The inequality in question (Lemma 2.4 of the Mode A draft)

In a free zone with Strength S₀, for suitable cut-offs φ, the draft asserted

$$
\int \boldsymbol{\omega}\cdot(\mathbf{e}\,\boldsymbol{\omega})\,\phi^2\,dx
\;\le\; -\,c\,S_0\int |u|^2\,\phi^2\,dx
\;+\; C_{\mathrm{geo}}\int |u|^2|\nabla\phi|^2\,dx
\;+\; C'\int |\nabla u|^2\,\phi^2\,dx .
$$

The **negative leading term** −c S₀ ∫|u|²φ² was the heart of Mode A: fed into the pressure estimate it would raise the ε-regularity threshold linearly in S₀, shrinking the CKN covering constant by a factor ∝ (1 + c S_min).

---

## Why the sign is not obvious

The vortex-stretching density ω·**e**·ω is, in a region of strong axial stretching, typically **positive** — stretching amplifies vorticity. This is the very mechanism that drives potential singularity formation. Asserting an integrated bound ≤ −c S₀ ∫|u|² (negative) requires that the shear component suppress stretching **more** than stretching amplifies vorticity.

That is a genuine inequality between two competing effects, not a normalization. The draft's Appendix A only sketched the absorption ("three steps: integration by parts, extraction of the leading positive term, absorption using shear and the controlled geometric flux"). The decisive sign was asserted, not derived.

---

## Internal conflict that had to be resolved first

The program contains a second inequality for the same quantity with the **opposite** sign — a *lower* bound of the form

$$
\int_U \boldsymbol{\omega}\cdot\mathbf{e}\cdot\boldsymbol{\omega}\,dx \;\gtrsim\; c\,J_{\mathrm{geo}}(U,t) - (\text{error}),
$$

arising on the C_small / blow-up side of the theory (it is what drives the ODE blow-up criterion). One quantity, two inequalities pulling in opposite directions. These apply to different classes (C_free vs C_small) under different hypotheses; clarifying this was a prerequisite, not an afterthought.

---

## The falsifiable numerical test (designed to disprove, not confirm)

The step was attacked by a test designed to be able to **disprove** the inequality:

1. **Scan a 2D parameter map**: shear strength |e_rθ| × axial stretching |e_zz|, moderate to strong.
2. At each point compute the sign of ∫ ω·**e**·ω.
3. Check whether the region where the sign is **negative** coincides with the C_free definition.
4. Use **worst-case vorticity**: take ω aligned with the stretching axis ξ₁, where ω·**e**·ω is maximally positive. If the sign is negative even there, the mechanism is robust; if not, the inequality is false as stated.

Three outcomes, all informative:
- negative sign exactly on C_free → mechanism confirmed;
- negative sign only elsewhere → the free-zone definition must change to match the physics;
- never negative at physical parameters → Lemma 2.4 is false as stated and Mode A must be rebuilt.

**Caveat.** The sign of ω·**e**·ω depends strongly on the orientation of ω relative to the eigenframe of **e**; ω must not be fixed arbitrarily. Either average over a physical ω distribution or use the worst case above.

---

## Historical assessment (pre-closure)

Rigor of this step at the time: **~35%** (a logical schema existed; the decisive sign was unproven). Any status label of "100%" or "closed" for Mode A that ignored this was inflation. This assessment is retained as the record of how the step stood before the two updates below settled it negatively.

---

## Update (2026-06-15): the vortex-stretching route is closed

A candidate mechanism for the negative sign was proposed (shear-layer cross term): with the strain tensor in a shear layer and small axial stretching $|a| \ll s$,
$$
\boldsymbol{\omega}\cdot\mathbf{e}\cdot\boldsymbol{\omega} = a\left(\omega_x^2 - \tfrac12\omega_y^2 - \tfrac12\omega_z^2\right) + s\,\omega_x\omega_y,
$$
the decomposition being correct, with the cross term $s\,\omega_x\omega_y$ dominant when $a \ll s$. The proposal was that this cross term is periodically negative through an oscillatory evolution of $\omega_x,\omega_y$.

**This route is refuted under consistent dynamics.** The oscillation was an artifact of an inconsistent setup: it used the rotation-only dynamics $\dot\omega_x = \tfrac{s}{2}\omega_y,\ \dot\omega_y = -\tfrac{s}{2}\omega_x$ (a purely antisymmetric matrix) for the vorticity, while evaluating $\boldsymbol{\omega}\cdot\mathbf{e}\cdot\boldsymbol{\omega}$ with the full strain. Under the consistent vortex equation $d\boldsymbol{\omega}/dt = (\mathbf{e}+\boldsymbol{\Omega})\boldsymbol{\omega}$:

- the $2\times2$ system for $(\omega_x,\omega_y)$ has discriminant $9a^2/4 + s^2 > 0$, hence **real eigenvalues** $\{a,\,-a/2\}$ — a saddle, not a center; there is no sustained oscillation;
- the vorticity aligns with the growing eigendirection, where $\omega_x\omega_y \to +s^2/8 > 0$;
- the time-average of the cross term is therefore **not** negative: it is zero in the degenerate $a=0$ case and positive for $a \neq 0$.

Three independent checks (eigenvalue analysis, direct numerical integration giving normalized $\langle\omega_x\omega_y\rangle \to +0.5$, and identification of the inconsistency) agree. The vorticity-stretching term does not supply the required integrated negative sign; the original difficulty — that vortex stretching is positive in stretching regions — stands.

**What remains usable:** the decomposition above is correct, and the observation that the cross term dominates when $a \ll s$ is valid. What fails is the claim of a negative *sign* from the stretching term.

---

## Update (2026-06-15, part 2): the pressure route is also closed — rigorously, both pointwise and on average

After the vortex-stretching route, the remaining candidate was the nonlocal pressure term in the local energy inequality,
$$
T_p := \int p\,(u\cdot\nabla\phi^2)\,dx,
$$
which Mode A would need to be negative and proportional to Strength. This is now resolved by a rigorous argument (not a numerical tendency), with skepticism applied in both directions.

### Pointwise: $T_p$ is not sign-definite

Using incompressibility and integration by parts, $T_p = -\int(\nabla p\cdot u)\phi^2$. Substituting $\nabla p$ from the momentum equation and projecting onto $u$ gives the exact identity
$$
T_p = -\int \tfrac{|u|^2}{2}(u\cdot\nabla\phi^2)\,dx - \nu\int\!\big[\Delta\tfrac{|u|^2}{2} - |\nabla u|^2\big]\phi^2\,dx + \int \partial_t\tfrac{|u|^2}{2}\,\phi^2\,dx .
$$
Only the viscous term $+\nu\int|\nabla u|^2\phi^2$ is sign-definite; the convective and unsteady terms are not. Explicit fields realize **both** signs (Bernoulli: flow accelerating into falling pressure gives $T_p>0$; decelerating flow gives $T_p<0$). Hence no deterministic bound $T_p \le -c\,\mathrm{Strength}$ exists. The earlier numerical "9 of 15 negative" was an illustration of this exact fact, not evidence for a sign.

### On average: $\langle T_p\rangle$ is not sign-definite either

For a statistically stationary ensemble $\langle\partial_t(\cdot)\rangle = 0$, leaving a competition between the sign-definite viscous term $+\nu\langle\int|\nabla u|^2\phi^2\rangle > 0$ and the indefinite convective flux. Dimensional balance in a shear layer (thickness $\delta$, shear $s$) gives the ratio convective/viscous $\sim s\delta^2/\nu = \mathrm{Re}$. Therefore:

- at low Reynolds number ($\mathrm{Re}\ll1$) the positive viscous term dominates and $\langle T_p\rangle > 0$;
- at high Reynolds number the indefinite convective term dominates and the sign is not fixed.

A counterexample (low $\mathrm{Re}$) thus refutes any universal claim $\langle T_p\rangle < 0$. Numerical confirmation: with a smooth field (low-Re proxy) $\langle T_p\rangle = +0.30$; with a rough field (high-Re proxy) $\langle T_p\rangle = -0.22$ — the sign tracks the regime. The negative values seen at $N=48$–$64$ were a feature of a particular regime, not a universal property of free zones.

### Conclusion

Both the pointwise and the ensemble-averaged Mode A pressure mechanisms are **closed**. Together with the vortex-stretching result, there is no sign-definite negative contribution available — neither in vortex stretching, nor in the pressure term, nor in its average. The deterministic Mode A claim (a geometric refinement of the CKN covering constant via a negative screening term in free zones) does **not** hold as formulated.

This is a rigorous negative result, established with two-sided skepticism: each refutation was itself tested for the opposite conclusion (explicit counterexamples for the pressure sign; a low-Re counterexample for the average), and only the sign-indefiniteness survived. What remains conceivable is not Mode A but a strictly weaker, regime-conditional statement — an observation about a Reynolds-number range rather than a screening theorem; it is not pursued. Mode A is closed.
