# Roadmap and Status

**Last updated:** 2026-06-15 (release v1)

## Honest status of the proof chain for dim_H(E) < 1 (Mode B)

| # | Link | Status | Type |
|---|---|---|---|
| 1 | E ⊂ C_small (singularities lie outside free zones) — Lemma A3 | ~85% | two independent proofs |
| 2,3 | CKN ε-regularity; dim_H(E) ≤ 1 | classical | theorem |
| 4 | free zones separate C_small (Cantor mechanism) | reduces to 5 + 6,7 + 10 | mechanism |
| 5 | self-similar cascade (free zones present at all scales) | ~55–60%; **φ_free≈0.5, roughly scale-independent on resolved octaves (DNS, N=128)** | model; supported by DNS, still tied to open K41 |
| 6,7 | transversality (non-nested gaps across scales) | ~50% | requires DNS; class formulation under revision |
| 8,9 | decorrelation of eigenvector orientation, E\|cos\| ≈ ½ | ~70% skeleton; **confirmed on a real NS field by DNS** (E\|cos\|=0.44–0.49, N=128), see `../theory/dns_validation.md` | core, now NS-validated |
| 10 | Frostman: gaps ⟹ dimension formula | ~90% | standard geometric measure theory |

**Resulting formula** (under transversality): dim_H(E) = 1 + log₂(1 − φ_free), where φ_free is the volume fraction of free zones per scale.

The product of confidences across the chain is small: **Mode B is a well-supported conditional conjecture, not a proven theorem.** Its core (random-matrix decorrelation + Frostman + Lemma A3) is solid; the open links (5, 6, 7) are tied to open problems in turbulence theory, not to gaps in the present arguments.

## Status of Mode A (closed — rigorous negative result)

- Text of the draft is essentially complete (`article/mode_A_CKN_constant.md`), but the **mathematical core is now refuted**, rigorously and with two-sided skepticism (see [`../theory/open_problem_sign.md`](../theory/open_problem_sign.md)).
- The deterministic Mode A claim required a sign-definite negative screening term in free zones. It is shown that **no such term exists**: not in vortex stretching (the proposed oscillation is an artifact of inconsistent dynamics; the eigenvalues are real), and not in the pressure term (sign-indefinite pointwise, with explicit counterexamples both ways; and the ensemble average changes sign with Reynolds number).
- This is recorded as a **closed negative result** — a checkable statement that has been settled (refuted). The draft is retained as the record of the approach; it is not submittable as formulated.
- A strictly weaker, regime-conditional statement (a Reynolds-range observation) remains conceivable but is not a screening theorem and is not pursued.

## Positive result: reduced model generates intermittency (2026-06-16)

A minimal three-state stochastic model built from the strain classes (C_small stretching / C_free screening / C_large diffusion, with C_free as transitional hub) reproduces **anomalous scaling of structure functions** — concave $\zeta_p$, multifractal intermittency that K41 does not give. Verified: robust across randomized parameters (100% concave), statistically significant vs single-state ($p=0.0002$), and the anomaly vanishes without class structure (control $\approx 0$, the K41 value). See `../theory/reduced_model_intermittency.md`. This is a reduced model (sufficiency, not derivation from NS), and is the most publishable positive direction in the program (a minimal geometric generator of intermittency).

## Priorities

Mode A is closed (see above); the program's live line is now Mode B and the consolidation of its verified core.

1. **Mode B — sharpen the conditional result.** State precisely what is proven and under exactly which hypotheses: the chain dim_H(E) = 1 + log₂(1 − φ_free) given (i) the self-similar cascade (φ_free > 0 at all scales) and (ii) transversality of free-zone gaps. Separate the verified core (Lemma ODE-1, GOE decorrelation, Frostman, Lemma A3) from the conditional links (5, 6, 7) with honest confidence on each.
2. **Close Lemma A3 (85% → 95%):** a rigorous Lipschitz estimate for the vorticity direction from the C_free conditions. Pure PDE, independent of open turbulence problems.
3. **Align the free-zone definition** between the (retained) paper draft and the program: the draft uses strong stretching (C_small in program terms) under the name "free zone"; the program uses moderate anisotropy with shear. Resolve the naming.
4. **Links 5, 6, 7** are tied to open problems in turbulence (K41 / intermittency, transversality). Do not re-attack them analytically in cycles; either decompose into a verifiable sub-question or record the resource requirement (N ≥ 128 DNS) explicitly.

## Closed negative results (recorded to avoid revisiting)

- **Cone / distortion covering** for lowering dim_H: ruled out — Hausdorff dimension is invariant under the diffeomorphic flow map.
- **"Any φ_free > 0 ⟹ dim < 1"**: false — an artifact of ignoring nesting of gaps across scales; corrected to the transversality condition.
- **Degenerate classifiers**: the anisotropy ratio max|λ|/Σ|λ| ≡ ½ for traceless tensors, and the Lund–Rogers shape parameter ≡ 0 on Gaussian random-phase fields. Class structure of strain can therefore only be validated on genuine DNS data, not on synthetic fields.
