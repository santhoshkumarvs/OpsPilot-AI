def identify_root_causes(correlated_alerts):
    """
    Naive root cause identifier based on correlated alerts.
    Returns a list of potential root causes.
    """
    root_causes = []

    for alert in correlated_alerts:
        # Ensure each alert is a dictionary
        if isinstance(alert, tuple) and len(alert) == 2:
            alert = alert[1]  # extract the alert dict from (index, alert)

        if not isinstance(alert, dict):
            continue  # skip invalid entries

        if alert.get('metric') == 'cpu':
            root_causes.append({
                "service": alert.get("service"),
                "reason": "High CPU usage",
                "severity": alert.get("severity"),
                "timestamp": alert.get("timestamp")
            })
        elif alert.get('metric') == 'memory':
            root_causes.append({
                "service": alert.get("service"),
                "reason": "Memory usage spike",
                "severity": alert.get("severity"),
                "timestamp": alert.get("timestamp")
            })
        elif alert.get('metric') == 'latency':
            root_causes.append({
                "service": alert.get("service"),
                "reason": "High latency observed",
                "severity": alert.get("severity"),
                "timestamp": alert.get("timestamp")
            })

    return root_causes
