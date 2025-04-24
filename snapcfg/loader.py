import json
import yaml
from pathlib import Path

def load_file(path):
    path = Path(path)
    if path.suffix in [".yaml", ".yml"]:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    elif path.suffix == ".json":
        with open(path, 'r') as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")
