import pytest
from engine.renderer import render_template
from pathlib import Path
import tempfile

def test_render_template_success():
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = Path(tempdir) / "test-template.j2"
        test_file.write_text("Hello {{ name }}")

        # Patch the template directory lookup
        import engine.renderer as renderer
        renderer.env.loader.searchpath.insert(0, tempdir)

        rendered = render_template("test-template", {"name": "Katrina"})
        assert "Katrina" in rendered

def test_render_template_missing():
    with pytest.raises(Exception):
        render_template("nonexistent-template", {})
