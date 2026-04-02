import json
from datetime import datetime, timezone
from pathlib import Path

def write_provenance(path, script_name, config=None, outputs=None, notes=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "script": script_name,
        "config": config,
        "outputs": outputs or [],
        "notes": notes or ""
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
