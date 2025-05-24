import os
import yaml
from datetime import datetime

def init_project():
    print("🔧 Bootstrapping AutoPilotOps...")
    config = yaml.safe_load(open("config/config.yaml"))
    os.makedirs(config["data_path"], exist_ok=True)
    os.makedirs(config["log_path"], exist_ok=True)

    # INTERVIEW QUESTION (Stripe): Data versioning
    version_tag = datetime.now().strftime("%Y%m%d_%H%M")
    open(f'{config["data_path"]}/version_{version_tag}.txt', "w").write("Initialized dataset version\n")
    print(f"✅ Data folder and version initialized: {version_tag}")

if __name__ == "__main__":
    init_project()
