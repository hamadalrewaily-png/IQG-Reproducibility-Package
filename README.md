# IQG-Reproducibility-Package

Public Tier-0 / Tier-1 starter repository for **Informational Quantum Gravity (IQG)**.

This repository is designed to match the manuscript's staged reproducibility language and appendix structure:

- **Appendix AN**: symbols, units, operator conventions
- **Appendix AM**: canonical equation index
- **Appendix Q**: numerical exploration and qualitative sweeps
- **Appendix AQ**: staged reproducibility, masking, provenance, and public/gated boundaries

## Repository status

This release is a **public starter package**. It is intentionally limited to Tier-0 / Tier-1 content.

Included now:
- repository scaffold aligned with Appendix AQ
- documentation files (`README`, `METHODS`, `REFERENCE_MAP`)
- public environment declaration
- masked public configs
- provenance utilities
- public Appendix Q qualitative figures (Q1–Q5) as released image artifacts
- runner scripts that either regenerate outputs when public artifacts exist or generate clearly labeled placeholder notices when public numeric artifacts are not yet supplied

Not included publicly:
- exact parameter locks
- deterministic replay seeds
- calibration-sensitive bands
- device-specific bindings or hardware-tuning procedures
- hidden Tier-2 materials governed by the Responsible-Use Addendum

## Quick start

```bash
conda env create -f environment.yml
conda activate iqg-public
bash run_all.sh
```

Outputs are written to:
- `results/figures/`
- `results/tables/`
- `provenance/runs/`

## Public artifact classes in this release

1. **Redshift schematic**
   - config: `configs/redshift_public.yaml`
   - script: `scripts/reproduce_redshift.py`

2. **SBIA ignition demonstration**
   - config: `configs/sbia_ignite_public.yaml`
   - script: `scripts/reproduce_sbia_ignite.py`

3. **ICE clustering preview**
   - config: `configs/ice_cluster_public.yaml`
   - script: `scripts/reproduce_ice_cluster.py`

4. **Appendix Q qualitative figures**
   - script: `scripts/make_q_figures.py`
   - outputs: `results/figures/figure_q1.png` ... `figure_q5.png`

## Critical implementation rule

**SBIA gating acts only on local source/growth terms; it does not multiply transport, diffusion, continuity, or mass-conserving operators.**

## Before using this repository URL in the manuscript

Replace the manuscript placeholder `[GitHub URL]` with your final public repository URL and confirm that:
- the public files match the statements in Appendix AQ,
- the Tier definitions match the Data/Code Availability section,
- any newly released CSV/NPZ artifacts are added to `artifacts/`,
- `REFERENCE_MAP.md` is updated to reflect the final file names and figure numbering.

## Current public Appendix Q figure set
The public qualitative sweep figures currently exposed in this repository use notation aligned to the manuscript:
- Q1 uses **\(\lambda\)** for damping
- Q2 uses **\(\beta_S\)** for entropy-gradient coupling
- Q3 uses **\(\mu\)** for nonlinear self-structuring

These are public Tier-0 / Tier-1 qualitative regenerations and should not be interpreted as deterministic Tier-2 locked replays.
