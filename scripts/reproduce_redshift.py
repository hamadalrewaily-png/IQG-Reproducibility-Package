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

    csv_path = pathlib.Path("artifacts/redshift/csv/redshift_curve.csv")
    npz_path = pathlib.Path("artifacts/redshift/npz/redshift_arrays.npz")

    if csv_path.exists():
        data = np.genfromtxt(csv_path, delimiter=",", names=True)
        fig, ax = plt.subplots(figsize=(8,5))
        ax.plot(data["z"], data["y"], label="IQG public curve")
        ax.set_xlabel("Redshift z")
        ax.set_ylabel("Distance / arbitrary public units")
        ax.set_title("Public redshift schematic")
        ax.legend()
        fig.tight_layout()
        fig.savefig(out, dpi=180)
        plt.close(fig)
        note = "Generated from public CSV artifact."
    elif npz_path.exists():
        data = np.load(npz_path)
        fig, ax = plt.subplots(figsize=(8,5))
        ax.plot(data["z"], data["y"], label="IQG public curve")
        ax.set_xlabel("Redshift z")
        ax.set_ylabel("Distance / arbitrary public units")
        ax.set_title("Public redshift schematic")
        ax.legend()
        fig.tight_layout()
        fig.savefig(out, dpi=180)
        plt.close(fig)
        note = "Generated from public NPZ artifact."
    else:
        make_placeholder_figure(
            "Redshift schematic placeholder",
            "No sanitized public redshift CSV/NPZ artifact is present in this starter release. "
            "Add a released public artifact under artifacts/redshift/ to enable regeneration.",
            out
        )
        note = "Placeholder created; no public redshift artifact present."

    write_provenance(
        "provenance/runs/redshift_run.json",
        "reproduce_redshift.py",
        config=str(config_path),
        outputs=[str(out)],
        notes=note
    )

if __name__ == "__main__":
    main()
