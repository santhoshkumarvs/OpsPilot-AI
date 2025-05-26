import json

def write_summary(summary, path="incident_summary.json"):
    try:
        with open(path, "w") as f:
            json.dump({"incident_summary": summary}, f, indent=2)
        print(f"[✔] Incident summary written to {path}")
    except Exception as e:
        print(f"[✖] Failed to write summary: {e}")
