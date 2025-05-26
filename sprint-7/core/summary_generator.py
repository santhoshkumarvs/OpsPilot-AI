def generate_summary(correlated_alerts, root_causes):
    """
    Generates a plain text summary from correlated alerts and identified root causes.
    """
    summary_lines = ["🚨 Incident Summary Report 🚨\n"]

    summary_lines.append("🔗 Correlated Alerts:")
    for alert in correlated_alerts:
        summary_lines.append(f"- [{alert.get('severity').upper()}] {alert.get('service')} - {alert.get('message')} at {alert.get('timestamp')}")

    summary_lines.append("\n🛠️ Root Cause Analysis:")
    if root_causes:
        for cause in root_causes:
            summary_lines.append(f"- {cause.get('service')}: {cause.get('reason')} (Severity: {cause.get('severity')}, Time: {cause.get('timestamp')})")
    else:
        summary_lines.append("- No definitive root cause identified.")

    return "\n".join(summary_lines)
