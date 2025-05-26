from .log_parser import parse_logs

def run_triage():
    print("🔍 Parsing logs from logs/app.log")
    parse_logs("logs/app.log")
