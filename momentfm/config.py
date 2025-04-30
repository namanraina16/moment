import yaml
from argparse import Namespace
from pathlib import Path

_cfg_path = Path(__file__).with_name("config.yaml")
_raw = yaml.safe_load(_cfg_path.read_text())

# flatten or namespace however you like
cfg = Namespace(**_raw.get("model", {}),
                **_raw.get("data", {}),
                **_raw.get("train", {}))
