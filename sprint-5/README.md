# Sprint-5: Monitoring Stack with Prometheus, Grafana, and FastAPI

This sprint implements a full monitoring stack to track application health and performance using:

- **FastAPI** with `prometheus_client` metrics
- **Prometheus** for scraping metrics
- **Grafana** dashboards for visualization
- **Docker Compose** setup for easy orchestration

## ✅ Key Metrics Monitored

- **HTTP request count** per method and status
- **Request latency** (Histogram)
- **Error rates** over time
- **CPU/Memory usage** via `node_exporter`
- **Custom alerts** for latency, errors, OOM, and restarts

## 📊 Grafana Dashboards

Includes visualizations for:

- P95 latency
- Error rate trends
- CPU usage
- Resident memory
- Client response summaries

## 🔥 Alert Simulation

Simulate high-latency or 500 errors using `simulate_alerts.py` to verify alert rules in Prometheus/Grafana.

## 📁 Folder Structure

```text
sprint-5/
├── docker-compose.yml
├── main_monitoring.py
├── prometheus/
│   └── prometheus.yml
├── grafana/
│   └── dashboards/
│       └── monitoring_dashboard.json
│   └── provisioning/
│       ├── dashboards.yml
│       └── datasources.yml
├── simulate_alerts.py
├── monitoring_scenarios.md
└── README.md
