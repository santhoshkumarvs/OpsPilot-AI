
---

### ✅ `monitoring_scenarios.md`

```markdown
# ✅ 15 Production-Level Monitoring Scenarios (Explained)

Each issue listed below reflects real-world observability needs, how it was detected via metrics, and how it was resolved with production insights.

## 1. High Latency (P95 > 1s)
- **Metric**: `http_request_latency_seconds`
- **Dashboard**: Latency histogram & line chart (p95)
- **Detection**: Sharp rise in `/predict` endpoint latency
- **Fix**: Cached model in memory and added batch inference

## 2. Out Of Memory (OOM)
- **Metric**: container_memory_usage_bytes
- **Detection**: Prometheus showed spike before crash
- **Fix**: Memory profiling revealed large JSON parsing → replaced with streaming API

## 3. Rising 5xx Error Rates
- **Metric**: `http_requests_total{status_code="500"}`
- **Detection**: Increase in error count per minute
- **Fix**: FastAPI logs revealed race condition, added lock

## 4. CPU Spike > 95%
- **Metric**: `node_cpu_seconds_total`
- **Detection**: Prometheus alert and Grafana CPU graph
- **Fix**: Moved batch preprocessing off main thread

## 5. Application Restart Loop
- **Metric**: `process_start_time_seconds`
- **Detection**: Restart time kept resetting
- **Fix**: Missing DB ENV var caused container exit → fixed compose setup

## 6. Endpoint Not Used
- **Metric**: `http_requests_total{endpoint="/old-endpoint"}`
- **Detection**: 0 requests over 30 days
- **Fix**: Cleaned up dead code + removed Prometheus monitoring

## 7. Memory Leak
- **Metric**: RSS (resident memory size)
- **Detection**: Linearly growing memory
- **Fix**: Unclosed file handles → used `with open()` + gc.collect()

## 8. Sudden Drop in Traffic
- **Metric**: `http_requests_total`
- **Detection**: Sudden zero traffic for 5 min
- **Fix**: NGINX crashed silently → added liveness probe

## 9. High Disk I/O
- **Metric**: node_disk_io_time_seconds_total
- **Detection**: Grafana showed 100% usage
- **Fix**: ML model logging too verbose → added log rotation

## 10. Cache Ineffectiveness
- **Metric**: Cache hit/miss rate (custom)
- **Detection**: 90% miss rate
- **Fix**: Increased cache TTL, reduced eviction size

## 11. Slow External API
- **Metric**: Latency per third-party service
- **Detection**: 2.5s avg latency to external auth API
- **Fix**: Introduced circuit breaker and async retries

## 12. Incorrect Response Format
- **Metric**: None! Detected via `simulate_alerts.py` + HTTP 400 surge
- **Fix**: Broken contract in upstream schema version → added contract test

## 13. TLS Certificate Expiry
- **Metric**: `ssl_cert_not_after`
- **Detection**: Alert triggered at 7-day window
- **Fix**: Automated cert renewal with webhook notifier

## 14. DB Pool Exhaustion
- **Metric**: DB connection count (custom SQL exporter)
- **Detection**: Spike to 100% pool usage
- **Fix**: Added exponential backoff in retries + improved pooling config

## 15. Kubernetes Pod Throttling
- **Metric**: `container_cpu_cfs_throttled_seconds_total`
- **Detection**: Grafana showed throttling > 25%
- **Fix**: Increased CPU request/limit in deployment.yaml

---

