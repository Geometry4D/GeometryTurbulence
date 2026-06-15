# Repository Navigation Guide

**Geometric Singularity Program — 3D Navier–Stokes**

---

## How to Read This Repository

### Starting point

- [`README.md`](../README.md) — overview, objectives, key references

### Current research plan

- [`/program/program_v1.md`](../program/program_v1.md) — active development plan  
  *(superseded versions are in `/archive/`)*

### Article drafts

| File | Mode | Topic | Status |
|------|------|--------|--------|
| [`article/draft_v1.md`](../article/draft_v1.md) | A | CKN ε-regularity constant | Skeleton |

### Numerical scripts

| File | Purpose |
|------|---------|
| [`scripts/ckn_energy_check.py`](../scripts/ckn_energy_check.py) | Scaled energy A(r) on Burgers vortex |

### Archive

Superseded documents are moved to `/archive/` with the original filename retained.
No files are deleted — the archive preserves the intellectual history of the program.

---

## Commit Convention

```
[YYYY-MM-DD | iter N] Short description
```

- `iter N` is a per-document counter, not a global one.
- Use the document abbreviation as a prefix when relevant:
  - `[prog]` for `/program/`
  - `[art]` for `/article/`
  - `[scr]` for `/scripts/`

Example:
```
[2026-06-20 | iter 02] [prog] program_v2.md — Phase I tasks revised after Lin re-read
```

---

## Dependencies

- Python ≥ 3.10, NumPy, SciPy (for `/scripts/`)
- No LaTeX build system required yet; drafts are in Markdown
