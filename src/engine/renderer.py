from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape()
)

def render_template(template_name: str, params: dict) -> str:
    template = env.get_template(f"{template_name}.j2")
    return template.render(**params)
