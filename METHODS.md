# METHODS.md

## Scope

This file maps the manuscript's public-facing equations and rules to the implementation decisions used in the public Tier-0 / Tier-1 reproducibility package.

It is **not** a substitute for the full manuscript. Its purpose is operational.

## 1. Units and conventions

Global ceilings and any quantity derived directly from \(I_{PIF}\) are reported in **nats** by default:

\[
\mathrm{bits}=\frac{\mathrm{nats}}{\ln 2}.
\]

Local PDE simulations use:

\[
\rho \in \mathrm{bits}\,\mathrm{m}^{-3}.
\]

The operator convention follows the manuscript:

\[
\Box \equiv \frac{1}{c^2}\partial_{tt}-\nabla^2.
\]

Thermodynamic entropy and information remain distinct:
- \(S_{th}\): thermodynamic entropy / entropy-potential
- \(I\): information in bits or nats

The scalar threshold driver is:

\[
g_S \equiv \|\nabla S_{th}\|.
\]

Transport is represented by:

\[
\vec v = -\mu_S \nabla S_{th}.
\]

Coefficient roles remain fixed:
- \(\beta_S\): entropy-gradient coupling in source/reaction sectors
- \(\eta\): time-response weighting
- \(\eta_T\): entropy-curvature-to-time coupling in the time-vector sector

The two epsilon symbols remain distinct:
- \(\epsilon_{SBIA}\): SBIA smoothing width
- \(\varepsilon_T\): time-flow ignition threshold

## 2. Numerical admissibility

Where reaction-sector kinetics are used, the public package adopts the manuscript's polynomial local reaction form as an implementation anchor:

\[
R(\rho)=\lambda \rho-\mu \rho^2+\nu \rho^3.
\]

Continuum boundedness comes from the sign convention of the highest-order term.
Numerical admissibility comes from:
- timestep guardrails,
- optional sub-cycling,
- positivity projection,
- optional finite-cap protection in stress-test runs.

Positivity projection:

\[
\rho \leftarrow \max(\rho,0).
\]

## 3. SBIA gate

Public runs default to the smoothed gate

\[
H_{\epsilon_{SBIA}}(u)=\frac{1}{2}\left(1+\tanh\!\left(\frac{u}{\epsilon_{SBIA}}\right)\right),
\qquad
u=g_S-S_{crit}.
\]

The full gate is written as

\[
\Gamma(x,t)=H_{\epsilon_{SBIA}}\!\big(g_S(x,t)-S_{crit}\big)\,\xi(x,t),
\]

with \(\xi(x,t)\) bounded and non-negative.

### Placement rule (critical)

The gate multiplies only local source/growth terms:

\[
\partial_t\rho=\mathcal{T}[\rho]+\Gamma(x,t)\,\mathcal{R}[\rho].
\]

Here:
- \(\mathcal{T}[\rho]\): ungated transport / diffusion / continuity operators
- \(\mathcal{R}[\rho]\): local source or reaction terms

**SBIA gating acts only on local source/growth terms; it does not multiply transport, diffusion, continuity, or mass-conserving operators.**

## 4. Public artifact scripts

The public scripts in this repository follow one of two paths:

1. **Artifact-backed regeneration**
   - If public CSV/NPZ data exist under `artifacts/`, the script loads them and regenerates the released figure.

2. **Transparent placeholder path**
   - If the public numeric artifact has not yet been supplied, the script generates a clearly labeled placeholder figure stating that the corresponding sanitized public numeric artifact is not yet present.

This keeps the public runner honest while preserving the final directory and workflow structure expected by Appendix AQ.

## 5. Provenance logging

Each main public script writes a small JSON provenance record containing:
- UTC timestamp
- script name
- config file
- outputs
- notes
- artifact/backing status

These logs are written under `provenance/runs/`.

## 6. Seed policy

Tier-0 / Tier-1 public runs are seed-agnostic by default.
No deterministic replay seeds are embedded in the public configs.
Deterministic replay belongs to Tier-2 only.

