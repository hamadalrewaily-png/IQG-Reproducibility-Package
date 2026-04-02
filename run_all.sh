#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH="${PYTHONPATH:-}:."

echo "[1/5] Staging Appendix Q released figures..."
python scripts/make_q_figures.py

echo "[2/5] Regenerating / checking redshift schematic..."
python scripts/reproduce_redshift.py --config configs/redshift_public.yaml

echo "[3/5] Regenerating / checking SBIA ignition..."
python scripts/reproduce_sbia_ignite.py --config configs/sbia_ignite_public.yaml

echo "[4/5] Regenerating / checking ICE clustering preview..."
python scripts/reproduce_ice_cluster.py --config configs/ice_cluster_public.yaml

echo "[5/5] Verifying outputs..."
python scripts/verify_outputs.py

echo "Done."
