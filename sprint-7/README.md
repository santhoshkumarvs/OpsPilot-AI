# 🚨 AutoPilotOps - Sprint 7: Event Correlation & Incident Summarization

This sprint focuses on building a complete **Incident Management Pipeline** that performs:

### ✅ Features Included
- 🔗 Alert correlation across multiple services
- 🛠️ Root cause analysis (RCA) using log and metric patterns
- 📋 Incident summarization with timeline and severity context
- 📦 Outputs clean `incident_summary.json` for downstream tools
- 📂 Modularized design under `core/` with clean structure for extendability

---

### 🧠 Sample RCA Flow

Given alerts like:

- High latency in `auth-service`
- Memory spike in `auth-service`
- High CPU in `payments-service`

The system produces:

- 🔗 Correlated Events
- 🛠️ Root Cause List (service-wise)
- 📋 Full Markdown-like Incident Summary
- 💾 JSON written to `/output/incident_summary.json`

---

### 🚀 How to Run

```bash
cd sprint-7/
python3 main.py
