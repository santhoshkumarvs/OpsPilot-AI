from fastapi import FastAPI
from prometheus_client import Counter, Summary, generate_latest
import time
import random

app = FastAPI()

# Metrics
REQUEST_COUNT = Counter("http_requests_total", "Total number of HTTP requests", ["method", "endpoint"])
LATENCY_SUMMARY = Summary("http_latency_seconds", "Request latency in seconds", ["endpoint"])
ERROR_COUNT = Counter("http_error_total", "Total number of simulated errors", ["endpoint"])
CPU_LOAD = Counter("cpu_spike_total", "Number of CPU spike simulations")

@app.get("/metrics")
def metrics():
    return generate_latest()

@app.get("/simulate_latency")
@LATENCY_SUMMARY.labels(endpoint="/simulate_latency").time()
def simulate_latency():
    REQUEST_COUNT.labels(method="GET", endpoint="/simulate_latency").inc()
    time.sleep(random.uniform(1, 3))  # simulate latency between 1 and 3 seconds
    return {"message": "Latency simulated"}

@app.get("/simulate_error")
def simulate_error():
    REQUEST_COUNT.labels(method="GET", endpoint="/simulate_error").inc()
    ERROR_COUNT.labels(endpoint="/simulate_error").inc()
    if random.random() > 0.5:
        return {"message": "No error"}
    else:
        return {"error": "Simulated error"}, 500

@app.get("/simulate_cpu")
def simulate_cpu():
    REQUEST_COUNT.labels(method="GET", endpoint="/simulate_cpu").inc()
    CPU_LOAD.inc()
    for _ in range(10_000_000):  # CPU churn
        pass
    return {"message": "CPU load simulated"}
