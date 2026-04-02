import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import pathlib, shutil
from scripts.common.provenance import write_provenance

def main():
    mapping = {
        "assets/original_figures/q1_lambda.png": "results/figures/figure_q1.png",
        "assets/original_figures/q2_betaS.png": "results/figures/figure_q2.png",
        "assets/original_figures/q3_mu.png": "results/figures/figure_q3.png",
        "assets/original_figures/q4_baseline_surface.png": "results/figures/figure_q4.png",
        "assets/original_figures/q5_baseline_heatmap.png": "results/figures/figure_q5.png",
    }
    outputs = []
    missing = []
    for src, dst in mapping.items():
        src_p = pathlib.Path(src)
        dst_p = pathlib.Path(dst)
        dst_p.parent.mkdir(parents=True, exist_ok=True)
        if src_p.exists():
            shutil.copy2(src_p, dst_p)
            outputs.append(str(dst_p))
        else:
            missing.append(src)
    note = "Copied released Appendix Q figures." if not missing else f"Missing: {missing}"
    write_provenance(
        "provenance/runs/appendix_q_run.json",
        "make_q_figures.py",
        config=None,
        outputs=outputs,
        notes=note
    )

if __name__ == "__main__":
    main()
