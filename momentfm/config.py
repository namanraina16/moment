import yaml
from argparse import Namespace
from pathlib import Path
from typing import Union, Any, Dict


class Config:
    """
    Load a YAML config file and expose:
      - config.model, config.data, config.train as Namespaces
      - config.as_flat_namespace() to merge all sections into one Namespace
    """

    def __init__(self, config_path: Union[str, Path] = None):
        # locate config.yaml next to this file by default
        if config_path is None:
            config_path = Path(__file__).with_name("config.yaml")
        self._path = Path(config_path)
        self._raw: Dict[str, Any] = yaml.safe_load(self._path.read_text()) or {}

        # for every top-level key in the YAML, wrap dicts in a Namespace
        for section, value in self._raw.items():
            if isinstance(value, dict):
                setattr(self, section, Namespace(**value))
            else:
                # non‐dict values you can access directly, e.g. cfg.version
                setattr(self, section, value)

    def as_flat_namespace(self) -> Namespace:
        """
        Merge all dict‐sections into a single Namespace.
        E.g. cfg_flat.learning_rate instead of cfg.train.learning_rate
        """
        flat: Dict[str, Any] = {}
        for value in self._raw.values():
            if isinstance(value, dict):
                flat.update(value)
        return Namespace(**flat)

    def __repr__(self) -> str:
        return f"<Config path={self._path!r} sections={list(self._raw.keys())}>"
