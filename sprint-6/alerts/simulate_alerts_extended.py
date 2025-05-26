import time
import random
import requests

METRICS_ENDPOINT = "http://localhost:8000/metrics"

def simulate_high_latency():
    for _ in range(5):
        response = requests.get("http://localhost:8000/simulate_latency")
        print("Simulated latency:", response.status_code)
        time.sleep(1)

def simulate_error_rate():
    for _ in range(5):
        response = requests.get("http://localhost:8000/simulate_error")
        print("Simulated error:", response.status_code)
        time.sleep(1)

def simulate_cpu_spike():
    for _ in range(5):
        response = requests.get("http://localhost:8000/simulate_cpu")
        print("Simulated CPU spike:", response.status_code)
        time.sleep(1)

if __name__ == "__main__":
    print("Simulating high latency...")
    simulate_high_latency()

    print("Simulating error rate...")
    simulate_error_rate()

    print("Simulating CPU spike...")
    simulate_cpu_spike()

    print("All simulations completed.")
