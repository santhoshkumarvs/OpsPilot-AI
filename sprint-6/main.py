from logs.triage_engine import run_triage
from remediation.auto_remediate import remediate

if __name__ == "__main__":
    print("[*] Running log triage...")
    run_triage()
    print("[*] Running auto-remediation checks...")
    remediate()
