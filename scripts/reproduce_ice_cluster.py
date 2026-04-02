import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import argparse, yaml, pathlib, numpy as np, matplotlib.pyplot as plt
from scripts.common.provenance import write_provenance
from scripts.common.plotting import make_placeholder_figure

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    config_path = pathlib.Path(args.config)
    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    out = pathlib.Path(cfg["outputs"][0])
    out.parent.mkdir(parents=True, exist_ok=True)

    csv_path = pathlib.Path("artifacts/ice_cluster/csv/ice_features.csv")
    npz_path = pathlib.Path("artifacts/ice_cluster/npz/ice_arrays.npz")

    if csv_path.exists():
        data = np.genfromtxt(csv_path, delimiter=",", names=True)
        fig, ax = plt.subplots(figsize=(7,5))
        if {"feature_x","feature_y"}.issubset(set(data.dtype.names)):
            ax.scatter(data["feature_x"], data["feature_y"], s=18)
        else:
            cols = data.dtype.names
            ax.scatter(data[cols[0]], data[cols[1]], s=18)
        ax.set_title("Public ICE clustering preview")
        fig.tight_layout()
        fig.savefig(out, dpi=180)
        plt.close(fig)
        note = "Generated from public CSV artifact."
    elif npz_path.exists():
        data = np.load(npz_path)
        fig, ax = plt.subplots(figsize=(7,5))
        ax.scatter(data["x"], data["y"], s=18)
        ax.set_title("Public ICE clustering preview")
        fig.tight_layout()
        fig.savefig(out, dpi=180)
        plt.close(fig)
        note = "Generated from public NPZ artifact."
    else:
        make_placeholder_figure(
            "ICE clustering placeholder",
            "No sanitized public ICE CSV/NPZ artifact is present in this starter release. "
            "Add a released public artifact under artifacts/ice_cluster/ to enable regeneration.",
            out
        )
        note = "Placeholder created; no public ICE artifact present."

    write_provenance(
        "provenance/runs/ice_run.json",
        "reproduce_ice_cluster.py",
        config=str(config_path),
        outputs=[str(out)],
        notes=note
    )

if __name__ == "__main__":
    main()
