## 🚑 Sprint-6: Auto-Remediation & Alert Enrichment

This sprint introduces automatic detection and response logic for service anomalies.

### Features:
- ⛑️ Auto-restart service on high latency
- ⚠️ Mock Slack alerts for high latency and CPU usage
- 🧠 Alert enrichment with recent log context
- 🧭 Conditional routing for `critical` vs `warning` alerts
- 🧪 Extended metrics simulation from `/simulate_latency`, `/simulate_cpu`, `/simulate_error`

### Key Logic:
- Auto-remediation triggered from `/metrics` data:
  - Latency > 2s → restart + critical Slack alert
  - CPU time > 1s → warning Slack alert
- Annotates alerts with last 5 error logs from FastAPI logs
- Runs continuously with safe handling for missing metrics

### Sample Output:
```bash
📊 Avg Latency: 3.15s, CPU Time: 0.97s
⚠️ Restarting dummy service...
📤 Sending Slack alert: High latency detected: 3.15s
  With context:
  [2025-05-26 12:00:12] ERROR: Something failed
