from pathlib import Path
import hashlib, sys

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    sums_file = Path("provenance/checksums/SHA256SUMS.txt")
    if not sums_file.exists():
        print("No SHA256SUMS.txt found.")
        sys.exit(1)
    ok = True
    for line in sums_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, rel = line.split("  ", 1)
        p = Path(rel)
        if not p.exists():
            print(f"MISSING: {rel}")
            ok = False
            continue
        got = sha256_of_file(p)
        if got != expected:
            print(f"MISMATCH: {rel}")
            ok = False
    print("OK" if ok else "FAILED")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
