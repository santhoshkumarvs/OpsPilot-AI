import re

def parse_logs(log_path):
    with open(log_path) as f:
        for line in f:
            if "ERROR" in line:
                print("[ERROR]", line.strip())
            elif "WARN" in line:
                print("[WARNING]", line.strip())
