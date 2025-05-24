import yaml
import importlib
from core.logger import logger

with open("sprint-4/core/configs/config.yaml", "r") as file:
    config = yaml.safe_load(file)

for stage in config["pipeline"]["stages"]:
    for attempt in range(config["pipeline"]["retries"]):
        try:
            module = importlib.import_module(f"core.pipeline.{stage[name]}")
            module.run()
            logger.info(f"{stage[name]} succeeded on attempt {attempt+1}")
            break
        except Exception as e:
            logger.error(f"{stage[name]} failed on attempt {attempt+1}: {e}")
            if attempt + 1 == config["pipeline"]["retries"]:
                logger.critical(f"{stage[name]} failed after {attempt+1} attempts")
