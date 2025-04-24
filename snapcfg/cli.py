import typer
from snapcfg.loader import load_file
from snapcfg.schema_parser import normalize_schema
from snapcfg.validator import validate_config
from rich import print

app = typer.Typer()

@app.command()
def validate(config: str, schema: str):
    cfg = load_file(config)
    raw_schema = load_file(schema)
    schema_obj = normalize_schema(raw_schema)
    try:
        validated = validate_config(cfg, schema_obj)
        print("[green]✅ Config is valid![/green]")
    except Exception as e:
        print(f"[red]❌ Validation error:[/red] {e}")
