import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import hashlib, pathlib, csv, json

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    required = [
        "results/figures/figure_q1.png",
        "results/figures/figure_q2.png",
        "results/figures/figure_q3.png",
        "results/figures/figure_q4.png",
        "results/figures/figure_q5.png",
        "results/figures/figure_redshift.png",
        "results/figures/figure_sbia_ignite.png",
        "results/figures/figure_ice_cluster.png",
    ]
    rows = []
    for rel in required:
        p = pathlib.Path(rel)
        rows.append({"path": rel, "exists": p.exists()})
    out_csv = pathlib.Path("results/tables/table_public_checks.csv")
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["path", "exists"])
        w.writeheader()
        w.writerows(rows)

    sums = []
    for rel in required:
        p = pathlib.Path(rel)
        if p.exists():
            sums.append(f"{sha256_of_file(p)}  {rel}")
    pathlib.Path("provenance/checksums").mkdir(parents=True, exist_ok=True)
    pathlib.Path("provenance/checksums/SHA256SUMS.txt").write_text("\n".join(sums) + ("\n" if sums else ""), encoding="utf-8")

if __name__ == "__main__":
    main()
