# REFERENCE_MAP.md

This file maps manuscript-facing artifacts to repository paths.

## Core public artifact classes

| Artifact class | Script | Config | Primary output |
|---|---|---|---|
| Redshift schematic | `scripts/reproduce_redshift.py` | `configs/redshift_public.yaml` | `results/figures/figure_redshift.png` |
| SBIA ignition demonstration | `scripts/reproduce_sbia_ignite.py` | `configs/sbia_ignite_public.yaml` | `results/figures/figure_sbia_ignite.png` |
| ICE clustering preview | `scripts/reproduce_ice_cluster.py` | `configs/ice_cluster_public.yaml` | `results/figures/figure_ice_cluster.png` |

## Appendix Q qualitative figure set

| Appendix Q figure | Current source | Released output |
|---|---|---|
| Figure Q1 — damping / lambda sensitivity | `assets/original_figures/q1_lambda.png` | `results/figures/figure_q1.png` |
| Figure Q2 — entropy-gradient coupling / beta_S sensitivity | `assets/original_figures/q2_betaS.png` | `results/figures/figure_q2.png` |
| Figure Q3 — nonlinear self-structuring / mu sensitivity | `assets/original_figures/q3_mu.png` | `results/figures/figure_q3.png` |
| Figure Q4 — baseline 3D evolution | `assets/original_figures/q4_baseline_surface.png` | `results/figures/figure_q4.png` |
| Figure Q5 — baseline propagation heatmap | `assets/original_figures/q5_baseline_heatmap.png` | `results/figures/figure_q5.png` |

## Status note

In this starter public release:
- the Appendix Q figure images are included as released visual artifacts,
- the artifact-backed public regeneration path for redshift / SBIA / ICE is scaffolded,
- sanitized public numeric arrays can later be added under `artifacts/` without changing the public file layout.

## Appendix Q public figure mapping (updated)

- **Figure Q1** → `results/figures/figure_q1.png`  
  Public qualitative damping sweep using **\(\lambda\)**.

- **Figure Q2** → `results/figures/figure_q2.png`  
  Public qualitative entropy-gradient coupling sweep using **\(\beta_S\)**.

- **Figure Q3** → `results/figures/figure_q3.png`  
  Public qualitative nonlinear self-structuring sweep using **\(\mu\)**.

- **Figure Q4** and **Figure Q5** remain the baseline evolution / propagation public artifacts already included in the package.
