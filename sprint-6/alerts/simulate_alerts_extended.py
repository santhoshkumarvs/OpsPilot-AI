# sprint-6/alerts/simulate_alerts_extended.py
import time
import random
import logging
from prometheus_client import Counter, Histogram, start_http_server

REQUEST_LATENCY = Histogram("http_request_latency_seconds", "Latency per request", ["endpoint"])
LOG_ERRORS = Counter("app_log_errors_total", "Count of log error lines")

def simulate_latency():
    while True:
        endpoint = random.choice(["/predict", "/inference", "/"])
        latency = random.choice([0.6, 1.2, 0.8, 0.3, 0.05])  # Inject spikes
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)
        print(f"Simulated latency {latency}s on {endpoint}")
        time.sleep(0.8)

def simulate_log_errors():
    errors = ["ConnectionError", "TimeoutError", "KeyError"]
    while True:
        if random.random() < 0.3:  # Inject error 30% of the time
            error_type = random.choice(errors)
            LOG_ERRORS.inc()
            logging.error(f"Simulated {error_type}")
        time.sleep(1.2)

if __name__ == "__main__":
    start_http_server(8081)  # exposes metrics at :8081/metrics
    print("🚀 Simulating alerts on http://localhost:8081/metrics")
    from threading import Thread
    Thread(target=simulate_latency).start()
    Thread(target=simulate_log_errors).start()
