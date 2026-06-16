# Roadmap and Status

**Last updated:** 2026-06-15 (release v1)

## Honest status of the proof chain for dim_H(E) < 1 (Mode B)

| # | Link | Status | Type |
|---|---|---|---|
| 1 | E ⊂ C_small (singularities lie outside free zones) — Lemma A3 | ~85% | two independent proofs |
| 2,3 | CKN ε-regularity; dim_H(E) ≤ 1 | classical | theorem |
| 4 | free zones separate C_small (Cantor mechanism) | reduces to 5 + 6,7 + 10 | mechanism |
| 5 | self-similar cascade (free zones present at all scales) | ~55% | model; tied to open K41 / intermittency |
| 6,7 | transversality (non-nested gaps across scales) | ~50% | requires DNS; class formulation under revision |
| 8,9 | random-matrix decorrelation of eigenvector orientation, E\|cos\| = ½ | ~70% | theorem skeleton + numerics — **core** |
| 10 | Frostman: gaps ⟹ dimension formula | ~90% | standard geometric measure theory |

**Resulting formula** (under transversality): dim_H(E) = 1 + log₂(1 − φ_free), where φ_free is the volume fraction of free zones per scale.

The product of confidences across the chain is small: **Mode B is a well-supported conditional conjecture, not a proven theorem.** Its core (random-matrix decorrelation + Frostman + Lemma A3) is solid; the open links (5, 6, 7) are tied to open problems in turbulence theory, not to gaps in the present arguments.

## Status of Mode A (first publication target)

- Text of the draft is essentially complete (`article/mode_A_CKN_constant.md`).
- **Mathematical core is open:** the main theorem rests on a geometric vortex-stretching inequality whose key *negative sign* is not yet proven (see [`../theory/open_problem_sign.md`](../theory/open_problem_sign.md)).
- Honest rigor of the core: ~35–40%, despite the text being complete. Text completeness ≠ proof completeness.

## Priorities

1. **Critical — resolve the sign** in the geometric vortex-stretching inequality (Mode A core). Numerical falsification test first: map the sign of ∫ω·e·ω over (shear × stretching) parameter space and check whether the negative region coincides with the free-zone definition.
2. Reconcile the two opposite-sign statements internal to the program (Lemma A3-side inequality vs. the Mode A inequality) before building on either.
3. Align the free-zone definition between the paper and the program (the paper currently describes strong stretching, i.e. C_small, under the name "free zone").
4. Close Lemma A3 (85% → 95%): a rigorous Lipschitz estimate for the vorticity direction from the C_free conditions. Pure PDE, independent of open turbulence problems.
5. DNS validation (JHTDB) of links 5, 6, 7 — requires external data access.

## Closed negative results (recorded to avoid revisiting)

- **Cone / distortion covering** for lowering dim_H: ruled out — Hausdorff dimension is invariant under the diffeomorphic flow map.
- **"Any φ_free > 0 ⟹ dim < 1"**: false — an artifact of ignoring nesting of gaps across scales; corrected to the transversality condition.
- **Degenerate classifiers**: the anisotropy ratio max|λ|/Σ|λ| ≡ ½ for traceless tensors, and the Lund–Rogers shape parameter ≡ 0 on Gaussian random-phase fields. Class structure of strain can therefore only be validated on genuine DNS data, not on synthetic fields.
