from datetime import datetime, timedelta

def extract_recent_errors(log_path="core/logs/server.log", window_minutes=5):
    try:
        with open(log_path, "r") as f:
            lines = f.readlines()
        now = datetime.now()
        threshold_time = now - timedelta(minutes=window_minutes)

        relevant_logs = [
            line for line in lines
            if "ERROR" in line and parse_log_time(line) > threshold_time
        ]
        return "\n".join(relevant_logs[-5:]) or "No recent ERROR logs."
    except Exception as e:
        return f"⚠️ Failed to extract log context: {e}"

def parse_log_time(line: str):
    try:
        timestamp = line.split(" - ")[0]
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S,%f")
    except Exception:
        return datetime.now()
