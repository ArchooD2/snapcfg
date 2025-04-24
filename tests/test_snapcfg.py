
import pytest
from snapcfg.loader import load_file
from snapcfg.validator import validate_config
from snapcfg.schema_parser import normalize_schema
import tempfile
import json
import yaml
from pathlib import Path

# Helpers to create temporary config and schema files
def write_temp_file(content, suffix):
    with tempfile.NamedTemporaryFile('w+', delete=False, suffix=suffix) as f:
        if suffix in ['.json', '.yaml', '.yml']:
            if suffix == '.json':
                json.dump(content, f)
            else:
                yaml.dump(content, f)
        else:
            f.write(content)
        f.flush()
        return f.name

def test_load_json():
    data = {"name": "test"}
    path = write_temp_file(data, ".json")
    loaded = load_file(path)
    assert loaded == data

def test_load_yaml():
    data = {"name": "test"}
    path = write_temp_file(data, ".yaml")
    loaded = load_file(path)
    assert loaded == data

def test_validate_passes():
    cfg = {"port": 8080}
    schema = {"port": {"type": "int", "min": 1, "max": 65535, "required": True}}
    norm_schema = normalize_schema(schema)
    validated = validate_config(cfg, norm_schema)
    assert validated["port"] == 8080

def test_validate_fails_on_type():
    cfg = {"port": "not_an_int"}
    schema = {"port": {"type": "int", "required": True}}
    norm_schema = normalize_schema(schema)
    with pytest.raises(TypeError):
        validate_config(cfg, norm_schema)

def test_validate_applies_default():
    cfg = {}
    schema = {"debug": {"type": "bool", "default": False}}
    norm_schema = normalize_schema(schema)
    validated = validate_config(cfg, norm_schema)
    assert validated["debug"] is False
