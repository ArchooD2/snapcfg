def validate_config(cfg, schema):
    def check(key, val, rules):
        if rules.get("type") == "int":
            if not isinstance(val, int):
                raise TypeError(f"{key} must be an int, got {type(val).__name__}")
            if "min" in rules and val < rules["min"]:
                raise ValueError(f"{key} too small (min {rules['min']})")
            if "max" in rules and val > rules["max"]:
                raise ValueError(f"{key} too large (max {rules['max']})")
        elif rules.get("type") == "str":
            if not isinstance(val, str):
                raise TypeError(f"{key} must be a str, got {type(val).__name__}")
        elif rules.get("type") == "bool":
            if not isinstance(val, bool):
                raise TypeError(f"{key} must be a bool, got {type(val).__name__}")

    def walk(cfg_section, schema_section, path=""):
        validated = {}
        for key, rules in schema_section.items():
            full_key = f"{path}.{key}" if path else key
            if isinstance(rules, dict) and "type" in rules:
                if key not in cfg_section:
                    if rules.get("required", False):
                        raise KeyError(f"Missing required key: {full_key}")
                    else:
                        validated[key] = rules.get("default")
                        continue
                check(full_key, cfg_section[key], rules)
                validated[key] = cfg_section[key]
            else:
                validated[key] = walk(cfg_section.get(key, {}), rules, full_key)
        return validated

    return walk(cfg, schema)
