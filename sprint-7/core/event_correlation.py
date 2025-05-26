def correlate_events(alerts, logs, metrics):
    correlated = []

    for alert in alerts:
        enriched_alert = {
            "message": alert["message"],
            "metric": alert["metric"],
            "service": alert["service"],
            "severity": alert["severity"],
            "timestamp": alert["timestamp"],
            "value": alert["value"],
            "logs": [log for log in logs if log["service"] == alert["service"]],
            "metrics": [metric for metric in metrics if metric["service"] == alert["service"]],
        }
        correlated.append(enriched_alert)

    return correlated
