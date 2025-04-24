
# snapcfg

**snapcfg** is a minimal configuration validation tool for Python projects. It allows you to load JSON or YAML configuration files and validate them against a simple, JSON-like schema with type checks and constraints.

## Features

- ✅ Supports JSON and YAML config files
- 🧾 Simple schema format using Python dicts
- 🛠 CLI and Python API for validation
- 🧪 Validates types (`int`, `str`, `bool`), ranges, required fields, and defaults

## Installation

```bash
pip install snapcfg
```

Or from source:

```bash
git clone https://github.com/yourname/snapcfg.git
cd snapcfg
pip install .
```

## Usage

### CLI

```bash
snapcfg validate --config path/to/config.yaml --schema path/to/schema.yaml
```

### Python API

```python
from snapcfg.loader import load_file
from snapcfg.schema_parser import normalize_schema
from snapcfg.validator import validate_config

config = load_file("config.yaml")
schema = normalize_schema(load_file("schema.yaml"))
validated = validate_config(config, schema)
```

## Example

**config.yaml**
```yaml
port: 8080
debug: true
```

**schema.yaml**
```yaml
port:
  type: int
  min: 1
  max: 65535
  required: true
debug:
  type: bool
  default: false
```

## License

This project is licensed under the terms of the MPL-2.0 license.
