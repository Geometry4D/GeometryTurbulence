# On the Optimal ε-Regularity Constant in the Caffarelli–Kohn–Nirenberg Theorem

**Mode A — Draft v1**  
**Date:** 2026-06-15  
**Status:** Outline / skeleton

---

## Abstract

*(to be written)*

We investigate the sharp value of the ε-regularity constant ε₀ appearing in
the partial regularity theorem of Caffarelli, Kohn, and Nirenberg (1982) for
suitable weak solutions of the three-dimensional Navier–Stokes equations.
A geometric reinterpretation of the scaled-energy condition is proposed...

---

## 1. Introduction

The question of global regularity for the three-dimensional incompressible
Navier–Stokes equations remains one of the central open problems in analysis.
While Leray–Hopf weak solutions are known to exist globally, their smoothness
is not established. The fundamental partial regularity result of
Caffarelli–Kohn–Nirenberg [CKN82] asserts that the singular set S(u) of any
suitable weak solution has parabolic Hausdorff dimension at most 1, and in
particular has zero 1-dimensional parabolic Hausdorff measure.

The proof hinges on an *ε-regularity criterion*: smallness of a suitable
scale-invariant energy quantity at a parabolic cylinder implies local
boundedness of u. The precise value of the threshold ε₀ in this criterion
is not made explicit in [CKN82] or in the subsequent simplified proof of
Lin [Lin98]. The present work undertakes a careful tracking of constants
through the proof, with the aim of identifying geometric constraints on ε₀.

**Organisation.** Section 2 fixes notation and recalls the CKN framework.
Section 3 re-derives the ε-regularity lemma with explicit constants.
Section 4 discusses the geometric content of the threshold.
Section 5 presents conclusions and open questions.

---

## 2. Notation and Preliminaries

*(to be filled)*

- Parabolic cylinder: Q_r(x,t) = B_r(x) × (t − r², t)
- Suitable weak solution: satisfies the local energy inequality
- Singular set: S(u) = {(x,t) : u ∉ L^∞(U) for any neighbourhood U of (x,t)}

---

## 3. ε-Regularity with Explicit Constants

*(derivation in progress)*

**Lemma (ε-regularity).** There exists ε₀ > 0 such that if u is a suitable
weak solution and

    A(r) + C(r) + D(r) < ε₀

at a parabolic cylinder Q_r(x₀, t₀), then u ∈ L^∞(Q_{r/2}(x₀, t₀)).

Here:
- A(r) = (1/r²) ∫∫_{Q_r} |u|³ + |p|^{3/2} dx dt   (energy + pressure term)
- C(r) = (1/r)  ∫∫_{Q_r} |∇u|²                      (dissipation)
- D(r) = ...

---

## 4. Geometric Interpretation

*(planned section)*

---

## 5. Conclusions

*(to be written)*

---

## References

[CKN82] Caffarelli, L., Kohn, R., Nirenberg, L. Partial regularity of suitable
        weak solutions of the Navier–Stokes equations. Comm. Pure Appl. Math.
        35 (1982), 771–831.

[CF93]  Constantin, P., Fefferman, C. Direction of vorticity and the problem of
        global regularity for the Navier–Stokes equations. Indiana Univ. Math.
        J. 42 (1993), 775–789.

[Lin98] Lin, F. A new proof of the Caffarelli–Kohn–Nirenberg theorem.
        Comm. Pure Appl. Math. 51 (1998), 241–257.
