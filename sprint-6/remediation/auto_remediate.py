import psutil

def remediate(threshold=80.0):
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        if proc.info['cpu_percent'] > threshold:
            print(f"⚠️ Killing high CPU process: {proc.info}")
            proc.kill()
