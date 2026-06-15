# Development Plan — Version 1

**Program:** Geometric Theory of Singularities for 3D Navier–Stokes  
**Version:** 1  
**Date:** 2026-06-15  
**Status:** Initial outline

---

## Phase I — Foundations (Mode A)

**Goal:** Establish a tighter upper bound on the Hausdorff dimension of the
singular set S(u) ⊂ ℝ³ × (0, T) for a suitable weak solution u.

The CKN theorem (1982) gives dim_H(S(u)) ≤ 1. The current programme pursues
a sharper constant in the ε-regularity criterion:

> If the *scaled energy* at a parabolic cylinder Q_r(x,t) satisfies
>
>     (1/r²) ∫∫_{Q_r} |u|³ dx dt  <  ε₀,
>
> then u is regular at (x, t).

**Open question (Mode A):** What is the optimal value of ε₀, and what
geometric structure does the level set {u : scaled energy = ε₀} carry?

### Immediate tasks

- [ ] Re-derive the CKN ε-regularity lemma with explicit constant tracking
- [ ] Compare with Lin (1998) simplified proof — identify slack in estimates
- [ ] Draft Section 1 of article: problem statement and known results

---

## Phase II — Geometric Criteria (Mode B)

**Goal:** Connect Constantin–Fefferman (1993) vorticity-direction regularity
to the capacity-theoretic singular set.

Key object: the vorticity direction field ξ = ω/|ω| where ω = curl u.

**Conjecture under investigation:** A geometric condition on the Lipschitz
regularity of ξ near a point (x₀, t₀) is sufficient to exclude singularity
at that point, and necessary in a measure-theoretic sense.

### Immediate tasks

- [ ] Formalize the Lipschitz-ξ condition in the CKN framework
- [ ] Identify whether CF condition implies CKN ε-regularity or is independent

---

## Phase III — Numerical Exploration (Mode C)

**Goal:** Probe scaling near potential singularities in simplified models
(axisymmetric NS, Burgers vortex perturbations).

See `/scripts/` for current experiments.

---

## Notes

This plan is versioned. Superseded versions are moved to `/archive/`.
Next version: `program_v2.md` when Phase I tasks are substantially complete.
