from snaparg.snaparg import SnapArgumentParser as ArgumentParser
from snapcfg.loader import load_file
from snapcfg.schema_parser import normalize_schema
from snapcfg.validator import validate_config

def main():
    parser = ArgumentParser(description="Validate configuration files.")
    parser.add_argument('--config', required=True, help="Path to config file (YAML/JSON)")
    parser.add_argument('--schema', required=True, help="Path to schema file (YAML/JSON)")
    args = parser.parse_args()

    config = load_file(args.config)
    schema = normalize_schema(load_file(args.schema))
    validated = validate_config(config, schema)
    
    print("✅ Config is valid!")
    print(validated)

if __name__ == "__main__":
    main()
