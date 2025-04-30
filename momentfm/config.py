# config.py
import yaml
from argparse import Namespace

with open("config.yaml") as f:
    raw = yaml.safe_load(f)

# flatten nested sections if you like, or keep them nested:
cfg = Namespace(
  **raw.get("model", {}),
  **raw.get("data", {}),
  **raw.get("train", {}),
)