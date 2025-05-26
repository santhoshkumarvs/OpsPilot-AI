import requests
import subprocess
import logging
import time
from log_parser import extract_recent_errors

PROMETHEUS_METRICS_URL = "http://localhost:8000/metrics"
MOCK_SERVICE_SCRIPT = "dummy_service.py"
LATENCY_THRESHOLD = 2.0
CPU_THRESHOLD = 5.0
MOCK_SLACK_CHANNEL = "#mock-alerts"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_metric(metric_name: str):
    try:
        response = requests.get(PROMETHEUS_METRICS_URL)
        if response.status_code != 200:
            return None
        for line in response.text.splitlines():
            if line.startswith(metric_name):
                parts = line.strip().split()
                return float(parts[-1])
    except Exception as e:
        logging.error(f"Error fetching metric {metric_name}: {e}")
    return None

def restart_service():
    logging.warning("🔁 Restarting dummy service due to health breach...")
    try:
        # Replace with actual restart command in real prod
        subprocess.run(["echo", "Mock restart of dummy service..."], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart service: {e}")

def send_mock_slack_alert(level, message, context):
    alert_msg = f"""
    🚨 [{level.upper()} ALERT] 🚨
    {message}

    🧠 Log Context:
    {context}

    📤 Sent to: {MOCK_SLACK_CHANNEL}
    """
    print(alert_msg)  # Replace with `requests.post(webhook, json=...)` for real Slack

def check_and_remediate():
    latency = fetch_metric("http_latency_seconds_sum")
    latency_count = fetch_metric("http_latency_seconds_count")
    cpu = fetch_metric("process_cpu_seconds_total")

    avg_latency = (latency / latency_count) if (latency and latency_count) else 0.0
    cpu = cpu if cpu is not None else 0.0

    logging.info(f"📊 Avg Latency: {avg_latency:.2f}s, CPU Time: {cpu:.2f}s")

    log_context = extract_recent_errors(log_path="core/logs/server.log")

    if avg_latency > LATENCY_THRESHOLD:
        restart_service()
        send_mock_slack_alert(
            level="critical",
            message=f"High latency detected: {avg_latency:.2f}s",
            context=log_context,
        )

    elif cpu > CPU_THRESHOLD:
        send_mock_slack_alert(
            level="warning",
            message=f"Elevated CPU usage detected: {cpu:.2f}s",
            context=log_context,
        )


    elif cpu > CPU_THRESHOLD:
        send_mock_slack_alert(
            level="warning",
            message=f"Elevated CPU usage detected: {cpu:.2f}s",
            context=log_context,
        )

if __name__ == "__main__":
    logging.info("🔍 Starting remediation monitor...")
    while True:
        check_and_remediate()
        time.sleep(10)  # check every 10 seconds
