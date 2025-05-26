import requests
import time

# Simulate high latency
print("Simulating latency...")
for _ in range(10):
    time.sleep(1.5)
    requests.get("http://localhost:8000/")

# Simulate error
print("Simulating errors...")
for _ in range(10):
    requests.get("http://localhost:8000/non-existent")

print("Simulation completed.")
