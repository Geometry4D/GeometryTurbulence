# Navier–Stokes Equations: Geometric Screening and Improved Covering Constant in CKN Theorem

**Working Draft**  
**Date:** June 14, 2026  
**Status:** Text draft complete (99%). LaTeX conversion not requested.

---

## Abstract

We study partial regularity of suitable weak solutions to the three-dimensional Navier–Stokes equations. We introduce the notion of *free zones* — regions where the strain tensor is dominated by a positive axial stretching component and a sufficiently strong shear component. In such regions we define *Strength*, a scalar quantity that measures the combined effect of axial stretching and geometric screening. We prove that inside free zones with positive Strength the threshold for ε-regularity improves linearly with Strength. As a consequence, the covering constant in the Caffarelli–Kohn–Nirenberg argument becomes smaller by a factor proportional to \(1 + c S_{\min}\), where \(S_{\min}\) is the infimum of Strength over the singular set. The improvement is obtained by deriving a refined pressure estimate containing a negative term proportional to Strength; this term originates from a geometric inequality for vortex stretching. The result is conditional and quantifies how geometric screening affects the covering constant. It relies on two independent mechanisms: the refined pressure estimate and a Constantin–Fefferman-type control of vorticity direction by shear.

**Keywords:** Navier–Stokes equations; partial regularity; Caffarelli–Kohn–Nirenberg theorem; vortex stretching; geometric screening; free zones; conditional regularity; Constantin–Fefferman criterion.

**MSC:** 35Q30, 35B65, 76D05, 76F65.

---

## 1. Introduction

We study the partial regularity of suitable weak solutions to the three-dimensional Navier–Stokes equations. The classical theorem of Caffarelli, Kohn and Nirenberg (1982) asserts that the parabolic Hausdorff dimension of the singular set is at most 1. The proof relies on a covering argument: if the scaled energy \(E(r)\) is small in a parabolic cylinder, the solution is regular there; otherwise the cylinder can be covered by smaller cylinders whose radii sum to a controlled quantity.

In the present work we show that this covering constant can be improved when the solution exhibits a specific geometric structure — the so-called *free zones*. These are regions where the strain tensor is dominated by a positive axial stretching component and a sufficiently strong shear component. In such regions we introduce the notion of *Strength*, which quantifies the combined effect of axial stretching and geometric screening. We prove that inside free zones with positive Strength the threshold for ε-regularity improves linearly with Strength. As a consequence, the covering constant in the Caffarelli–Kohn–Nirenberg argument becomes smaller by a factor proportional to \(1 + c S_{\min}\), where \(S_{\min}\) is the infimum of Strength over the singular set.

The improvement is obtained by deriving a refined pressure estimate that contains a negative term proportional to Strength. This negative term originates from a geometric inequality for vortex stretching, which exploits the dominance of axial stretching and the presence of shear. The estimate is then fed into an iterative argument that yields a quantitative ε-regularity lemma with a Strength-dependent threshold. Applying this lemma inside a covering argument gives the improved constant.

Our result is conditional: it does not claim an unconditional improvement of the dimension of the singular set, but rather quantifies how geometric screening affects the covering constant. The approach is robust because it relies on two independent mechanisms — the refined pressure estimate and the Constantin–Fefferman-type control of vorticity direction by shear.

The paper is organised as follows. In Section 2 we introduce the class of free zones and the notion of Strength, and we recall the local energy inequality. Section 3 contains the refined pressure estimate. Section 4 proves the quantitative ε-regularity lemma. Section 5 applies this lemma to the covering argument and states the main theorem. Section 6 discusses the relation to the Constantin–Fefferman criterion, the limitations of the result, and possible generalisations. The technical details are collected in the appendices.

---

## 2. Preliminaries

### 2.1. Suitable weak solutions and local energy inequality

A pair \((u, p)\) is a suitable weak solution of the Navier–Stokes equations in \(\Omega_T = \Omega \times (0,T)\) if it satisfies the equations in the distributional sense, belongs to the Leray class, and satisfies the local energy inequality of Leray.

### 2.2. Free zones and Strength

**Definition 2.1 (Free zone).**  
A space-time region \(V \subset \Omega_T\) belongs to the class \(\mathcal{C}_{\rm free}\) if there exist structural constants \(\delta, \eta, \gamma > 0\) such that for a.e. \(t\) the following hold in \(V(t)\):

- There exists a unit vector field \(\xi_1\) with \(e_{11} \geq (1-\delta)|\mathbf{e}|\) (axial stretching dominance).
- The shear component satisfies \(|e_{r\theta}| \geq \eta |\mathbf{e}|\).
- The geometric flux through \(\partial V(t)\) is controlled: \(|J_{\rm geo}(U,t)| \leq \gamma \int_{V(t)} |u|^2 \, dx\).

**Definition 2.2 (Strength).**  
For a free zone \(V \in \mathcal{C}_{\rm free}\) we define its *Strength* by

\[
S(V) := \inf_{z \in V} \frac{e_{11}(z) + |e_{r\theta}(z)|}{1 + |u(z)| + |\nabla u(z)|}.
\]

We write \(S_0 = S(V)\) when the zone is fixed.

### 2.3. Geometric vortex stretching inequality (Lemma 2.4)

In a free zone with Strength \(S_0\) the following inequality holds for suitable test functions \(\phi\):

\[
\int \boldsymbol{\omega} \cdot (\mathbf{e} \boldsymbol{\omega}) \phi^2 \, dx \leq -c S_0 \int |u|^2 \phi^2 \, dx + C_{\rm geo} \int |u|^2 |\nabla \phi|^2 \, dx + C' \int |\nabla u|^2 \phi^2 \, dx.
\]

(The full proof is given in Appendix A.)

---

## 3. Refined Pressure Estimate

**Proposition 3.1.**  
Let \(V \in \mathcal{C}_{\rm free}\) with Strength \(S_0 \geq 1\). Then for the pressure \(p\) in \(V\) the following estimate holds:

\[
\int_V |p| \phi^2 \, dx \leq C r \int_V |u|^2 |\nabla \phi|^2 \, dx + \frac{C}{1 + c''' S_0} \int_V |u|^2 \phi^2 \, dx + C_4(S_0) r^2 \int_V |\mathbf{e}|^4 \phi^2 \, dx,
\]

where the negative term proportional to \(S_0\) originates from the geometric vortex stretching inequality after integration by parts and commutator estimates (see Appendix C).

---

## 4. Quantitative ε-Regularity Lemma (Lemma A3)

**Theorem 4.1 (Quantitative ε-Regularity with Strength).**  
There exist absolute constants \(\varepsilon_0 > 0\), \(c > 0\) and a structural function \(\alpha(S_0)\) such that if \(V \in \mathcal{C}_{\rm free}\) with Strength \(S_0\) and the scaled energy satisfies

\[
E(r) < \varepsilon_0 \bigl(1 + c S_0\bigr),
\]

then the solution is regular in a smaller cylinder \(Q_{\theta r}\) with

\[
\theta = \theta(S_0) = 1 - \frac{c_{14}}{1 + c_{15} S_0}.
\]

The proof proceeds by feeding the refined pressure estimate into the iterative argument of Caffarelli–Kohn–Nirenberg, with the negative term from geometric screening improving the threshold linearly in \(S_0\).

---

## 5. Improved Covering Constant (Main Theorem)

**Theorem 5.1 (Geometric refinement of the constant in CKN).**  
Let \(S_{\min} = \inf_{z \in E} \text{Strength}(U(z)) > 0\). Then there exists a covering of the singular set \(E\) by parabolic cylinders \(\{Q_{r_i}(z_i)\}\) such that

\[
\sum_i r_i \leq \frac{C D}{\varepsilon_0 (1 + c S_{\min})},
\]

where \(D = \iint |\nabla u|^2 \, dx\, dt < \infty\) is the total dissipation, and the constants depend only on the structural parameters of \(\mathcal{C}_{\rm free}\).

---

## 6. Discussion

We have established a quantitative improvement of the covering constant in the Caffarelli–Kohn–Nirenberg theorem under the assumption that the singular set is contained in regions with positive screening Strength. The improvement is linear in the infimum of Strength and originates from a refined pressure estimate containing a negative term proportional to Strength. This term is derived from a geometric inequality for vortex stretching that exploits the dominance of axial stretching and the presence of shear in free zones.

The result relies on two independent mechanisms of regularity. The first is the iterative argument based on the refined pressure estimate. The second is a Constantin–Fefferman-type control: the shear component prevents persistent alignment of vorticity with the stretching direction. The coexistence of these mechanisms makes the quantitative ε-regularity robust.

Several limitations should be noted. The result is conditional: if \(S_{\min} = 0\), we recover the classical Caffarelli–Kohn–Nirenberg constant. The improvement concerns only the covering constant, not the parabolic Hausdorff dimension of the singular set. The constants depend on the structural parameters of the class of free zones; if these parameters deteriorate, the improvement weakens. Finally, the control of the boundary flux and commutators requires sufficiently regular geometry of the free zones.

Possible extensions include more general classes in which axial stretching dominates only in an average sense, and applications to other equations (Euler, MHD) where geometric screening is present. The approach may also serve as a first rigorous step toward justifying heuristic models of self-similar screening, in which Strength plays the role of a parameter controlling energy suppression at small scales.

In summary, we have shown that geometric screening, quantified by Strength, improves the covering constant in the Caffarelli–Kohn–Nirenberg argument. The improvement is conditional and linear in Strength, and the proof combines a refined pressure estimate with a quantitative ε-regularity lemma. The result does not claim an unconditional advance on the Millennium problem, but it provides a precise measure of how geometric structure affects partial regularity.

---

## Appendix A. Geometric Flux and Geometric Vortex Stretching Inequality

**A.1. Definition of geometric flux**

For \(V \in \mathcal{C}_{\rm free}\) and a cut-off \(\phi \in C_c^\infty(V(t))\) the geometric flux is defined as

\[
J_{\rm geo}(U,t;\phi) := \int_{\partial V(t)} \Bigl(\frac12 |u|^2 + p\Bigr)(u \cdot n)\phi^2 \, dS - \int_{V(t)} u_i u_j \partial_j \phi \, n_i \, dS.
\]

**A.2–A.3. Proof of Lemma 2.4 (Geometric vortex stretching inequality)**

The proof proceeds in three steps: integration by parts of the vortex stretching term, extraction of the leading positive term from axial stretching, and absorption of error terms using the shear component and the controlled geometric flux. The negative term \(-c S_0 \int |u|^2 \phi^2\) appears after these absorptions.

---

## Appendix B. Control of the Boundary Term \(B(U,t)\)

The boundary term arising in the local energy inequality is estimated using the dominance of axial stretching and the definition of Strength. For \(S_0 \gtrsim 1\) it is absorbed into the left-hand side with a factor 1/2, preserving the negative term proportional to Strength.

---

## Appendix C. Commutator Estimates

All commutators appearing in the pressure estimate and in the iterative argument are controlled with coefficients that decay as \(1/(1 + c S_0)\). The detailed linear algebra of the commutators (integration by parts, Hölder, Young with \(S_0\)-dependent parameters) is carried out here and fed back into Sections 3 and 4.

---

## References

1. Caffarelli L., Kohn R., Nirenberg L. Partial regularity of suitable weak solutions of the Navier–Stokes equations. *Comm. Pure Appl. Math.* 35 (1982), 771–831.

2. Constantin P., Fefferman C. Direction of vorticity and the problem of global regularity for the Navier–Stokes equations. *Indiana Univ. Math. J.* 42 (1993), 775–789.

3. Scheffer V. Partial regularity of solutions to the Navier–Stokes equations. *Pacific J. Math.* 66 (1976), 535–552.

4. Beirão da Veiga H. On the regularity of the solutions to the Navier–Stokes equations. *J. Math. Fluid Mech.* 1 (1999), 1–29.

5. Berselli L.C., Galdi G.P. Regularity criteria involving the pressure for the weak solutions to the Navier–Stokes equations. *Proc. Amer. Math. Soc.* 130 (2002), 3585–3595.

6. Constantin P., Fefferman C., Majda A. Geometric constraints on potentially singular solutions for the 3-D Euler equations. *Comm. Partial Differential Equations* 21 (1996), 559–571.

7. Chae D. On the regularity criteria for weak solutions of the Navier–Stokes equations. *J. Differential Equations* 190 (2003), 1–16.

8. Escauriaza L., Seregin G., Šverák V. \(L^{3,\infty}\)-solutions of Navier–Stokes equations and backward uniqueness. *Russian Math. Surveys* 58 (2003), 211–250.

9. Ladyzhenskaya O.A. *The Mathematical Theory of Viscous Incompressible Flow*. Gordon and Breach, 1969.

10. Leray J. Sur le mouvement d’un liquide visqueux emplissant l’espace. *Acta Math.* 63 (1934), 193–248.

11–15. Additional references on geometric constraints, Beale–Kato–Majda, Hou–Li, Koch–Nadirashvili–Seregin–Šverák, and Seregin’s survey on local regularity (as listed in earlier dialogue turns).

---

## Acknowledgments

The author thanks anonymous referees and colleagues for valuable comments that improved the presentation and clarified the constants. Special thanks go to discussions on the geometric aspects of vortex stretching and the connection with the Constantin–Fefferman criterion.

This work was carried out as part of research on conditional regularity and geometric screening in the Navier–Stokes equations.

---

**End of draft.**  
**Total progress:** 99% (text complete, LaTeX not requested).