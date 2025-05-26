from core.alert_loader import load_alerts
from core.event_correlation import correlate_events
from core.rca_engine import identify_root_causes
from core.summary_generator import generate_summary
from core.summary_writer import write_summary
from core.incident_summarizer import summarize_incident
from core.summary_writer import write_summary
import json


def main():
    # Load alerts
    alerts = load_alerts("alerts/simulated_alerts.json")
    
    # Load logs and metrics
    with open("data/sample_logs.json") as f:
        logs = json.load(f)
    
    with open("data/sample_metrics.json") as f:
        metrics = json.load(f)

    print("[✔] Alerts loaded:")
    print(alerts)

    # Run correlation
    correlated = correlate_events(alerts, logs, metrics)

    # Root Cause Analysis
    root_causes = identify_root_causes(correlated)

    # Generate Summary
    summary_text = generate_summary(correlated, root_causes)

    # Save summary
    write_summary(summary_text, path="incident_summary.json")

    # Enriched final summary
    enriched_summary = summarize_incident(summary_text, correlated, root_causes)


    print("\n[✔] Enriched Summary:\n", enriched_summary)


if __name__ == "__main__":
    main()
