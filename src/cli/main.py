# PATCHED: sentinel/src/cli/main.py

import typer
import yaml
from engine.renderer import render_template
from engine.validator import validate_policy
from engine.audit import push_audit, flush_log_queue
from supabase_client.templates import list_templates, pull_template

app = typer.Typer()

def parse_params(params):
    parsed = {}
    for p in params:
        if "=" not in p:
            raise ValueError(f"Invalid param format: {p}. Expected key=value.")
        k, v = p.split("=", 1)
        parsed[k] = v
    return parsed

@app.command()
def generate(template: str, params: list[str]):
    """
    Render a policy from template and params.
    Example: sentinel generate --template AllowAdmin --params user_id=123
    """
    try:
        param_dict = parse_params(params)
        rendered = render_template(template, param_dict)
        print(rendered)
        push_audit("generate", {"template": template, "params": param_dict}, {"policy": rendered})
    except Exception as e:
        print(f"❌ Error: {e}")

@app.command()
def validate(file: str):
    """
    Validate a YAML policy file.
    """
    try:
        policy = validate_policy(file)
        print("✅ Policy is valid:", policy)
        push_audit("validate", {"file": file}, {"valid": True})
    except Exception as e:
        print(f"❌ Invalid policy: {e}")
        push_audit("validate", {"file": file}, {"valid": False, "error": str(e)})

@app.command()
def push(file: str):
    """
    Push a validated policy to Supabase.
    """
    try:
        with open(file, "r") as f:
            content = yaml.safe_load(f)
        push_audit("push", {"file": file}, {"content": content})
        print("✅ Policy pushed to Supabase")
    except Exception as e:
        print(f"❌ Push failed: {e}")

@app.command()
def templates():
    """
    List or pull templates from Supabase.
    """
    try:
        cmd = typer.prompt("Choose 'list' or 'pull'")
        if cmd == "list":
            templates = list_templates()
            for t in templates:
                print(f"{t['id']} - {t['name']}")
        elif cmd == "pull":
            template_id = typer.prompt("Enter Template ID")
            tpl = pull_template(template_id)
            print("📄 Template:", tpl["template"])
        else:
            print("❌ Unknown subcommand. Use 'list' or 'pull'")
    except Exception as e:
        print(f"❌ Template command failed: {e}")

@app.command()
def sync():
    """
    Flush offline audit logs to Supabase from .sentinel/logs/queue.json
    """
    try:
        flush_log_queue()
        print("✅ Offline audit logs synced to Supabase")
    except Exception as e:
        print(f"❌ Sync failed: {e}")
