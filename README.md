# Geometric Singularity Program — 3D Navier–Stokes Equations

**Research program on regularity theory and potential finite-time singularities  
via geometric and capacity-theoretic methods.**

---

## Overview

This repository hosts an ongoing research program investigating the regularity and
potential finite-time blow-up of solutions to the three-dimensional incompressible
Navier–Stokes equations:

```
∂ₜu + (u · ∇)u = −∇p + ν Δu,    ∇ · u = 0,    (x, t) ∈ ℝ³ × (0, T).
```

The central objects of study are the *singular set* of a suitable weak solution and
the geometric–measure-theoretic constraints that govern its structure. The program
draws on the framework of Caffarelli–Kohn–Nirenberg (1982) and the geometric
vorticity criterion of Constantin–Fefferman (1993) as its two principal pillars.

> **Status: active research program.**  
> No theorem proving global regularity or finite-time blow-up is claimed at this stage.  
> All documents are working drafts subject to revision without notice.

---

## Scientific Objectives

| # | Objective | Current mode |
|---|-----------|--------------|
| A | Sharpen the dimensional bound on the singular set via an improved CKN constant | Article draft (`/article`) |
| B | Geometric characterisation of potential blow-up via vorticity-direction alignment | Theory (`/program`) |
| C | Numerical exploration of near-singular behaviour and critical scaling | Scripts (`/scripts`) |

---

## Repository Structure

```
/program   — versioned development plans (program_vN.md)
/article   — manuscript drafts  [Mode A: CKN constant refinement]
/scripts   — numerical experiments and verification (Python / NumPy / SciPy)
/docs      — navigation guide, executive summaries, supplementary notes
/archive   — superseded versions of plans and drafts
```

See [`/docs/navigation.md`](docs/navigation.md) for a detailed map of the repository.

---

## Key References

1. **Caffarelli, L., Kohn, R., Nirenberg, L.** (1982).  
   *Partial regularity of suitable weak solutions of the Navier–Stokes equations.*  
   Comm. Pure Appl. Math. **35**(6), 771–831.  
   doi:[10.1002/cpa.3160350604](https://doi.org/10.1002/cpa.3160350604)

2. **Constantin, P., Fefferman, C.** (1993).  
   *Direction of vorticity and the problem of global regularity for the Navier–Stokes equations.*  
   Indiana Univ. Math. J. **42**(3), 775–789.  
   doi:[10.1512/iumj.1993.42.42034](https://doi.org/10.1512/iumj.1993.42.42034)

3. **Fefferman, C.** (2000).  
   *Existence and smoothness of the Navier–Stokes equation.*  
   Clay Mathematics Institute Millennium Problem statement.  
   [claymath.org](https://www.claymath.org/millennium/navier-stokes-equation/)

4. **Lin, F.** (1998).  
   *A new proof of the Caffarelli–Kohn–Nirenberg theorem.*  
   Comm. Pure Appl. Math. **51**(3), 241–257.

---

## Commit Convention

Structured commit messages are used throughout:

```
[YYYY-MM-DD | iter N] Short description of change
```

Example:
```
[2026-06-15 | iter 01] Add program_v1.md — initial research plan
```

---

## License

All rights reserved. This is a private research repository.  
Contact the author before citing or reproducing any content.
