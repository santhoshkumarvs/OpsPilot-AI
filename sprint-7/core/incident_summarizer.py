# sprint-7/core/incident_summarizer.py

def generate_summary(rca_output, alerts):
    """
    Generate a human-readable incident summary from root cause and alerts.
    """
    impact = "unknown"
    recommendations = []

    if alerts:
        impact = "High" if any(alert["severity"] == "critical" for alert in alerts) else "Medium"

    if "root_cause" in rca_output:
        for component, cause in rca_output["root_cause"].items():
            if "CPU" in cause:
                recommendations.append(f"Scale up CPU for {component}")
            elif "Memory" in cause:
                recommendations.append(f"Investigate memory usage in {component}")
            else:
                recommendations.append(f"Review component: {component}")

    # core/incident_summarizer.py

def summarize_incident(summary_text, correlated_events, root_causes=None):
    summary = {
        "summary": summary_text,
        "incident_cause": root_causes or [],
        "correlated_events": correlated_events,
    }
    return summary


