# Development Log

The iteration-by-iteration history of the program, kept separate from the mathematical core so that `theory/` stays clean. This log records the reasoning, including discarded approaches — the negative results are part of the scientific record.

## Methodological note

The program advances by proposing a mechanism, testing it numerically with an eye to **falsification**, and only then promoting it to a claim. Over the recorded development, **seven** candidate results were caught and corrected by skeptical checking *before* entering the body of established results. Confidence percentages were lowered, not raised, whenever a gap was found. This is recorded deliberately as the working discipline of the program.

## The seven corrections (skeptical checks that changed course)

1. **Cone / distortion covering is a dead end** — Hausdorff dimension is invariant under the diffeomorphic flow map, so distortion covering cannot lower it. (Redirected the program to the spatial-gap mechanism.)
2. **Lemma A3 ↔ early ER contradiction** — an early version placed singularities in free zones, contradicting A3; corrected to E ⊂ C_small with free zones *separating* the singular set.
3. **RPA breakdown in coherent structures** — the forcing decorrelation argument fails where coherent structures live; replaced by the observation that the *class* (geometry) decorrelates even when the forcing (amplitude) does not.
4. **Nyquist artifact** — a spurious phase alignment (0.68) near the grid Nyquist scale; vanished (→ 0.02–0.05) at larger grids.
5. **C_small ↔ E conflation** — the self-similar-cascade argument briefly conflated the strain class C_small (positive-volume) with the singular set E (dim ≤ 1); the resulting "improvement" was withdrawn.
6. **Two degenerate classifiers** — the anisotropy ratio max|λ|/Σ|λ| ≡ ½ for traceless strain, and the Lund–Rogers parameter ≡ 0 on Gaussian random-phase fields. Consequence: class structure can only be validated on genuine DNS, not synthetic fields; the "class-nesting" numerics were reassessed.
7. **Naive orientation formula** — dim = 3 + log₂ p, which conflated measure with dimension and ignored the scale-dependence of vorticity; withdrawn, the orientation route kept only as an idea.

## Arc of the program

- **Early:** the ambitious target dim_H < 1 was pursued via cones/distortion (regime C). This was closed as topologically impossible (correction 1).
- **Middle:** the correct architecture was identified — free zones *separate* the singular set via spatial gaps (Cantor mechanism), routed through CKN ε-regularity rather than flow transport (correction 2). The Frostman link was made rigorous; the random-matrix decorrelation of eigenvector orientation emerged as the solid core.
- **Reassessment:** the degenerate-classifier findings (correction 6) showed that synthetic fields cannot validate the class structure; the honest status of the conditional links was lowered accordingly. The eigenvector-orientation result survived because it does not depend on the class classifier.
- **Mode A draft:** the provable regime (refinement of the CKN constant) was written up to full text, and review located its single open step — the sign in the vortex-stretching inequality (`../theory/open_problem_sign.md`).

## Honest overall status

dim_H(E) < 1 (Mode B) is a well-supported conditional conjecture with a solid core (random-matrix decorrelation + Frostman + Lemma A3) and open links (self-similar cascade, transversality) tied to open problems in turbulence theory. Mode A is text-complete but rests on the unproven sign. Neither is a finished theorem; both rest on a verified technical core.

## Next steps

See `../program/01_roadmap.md`. The single most valuable next step is resolving the sign in the vortex-stretching inequality (numerical falsification test, then a PDE specialist).
