import subprocess
import pytest
from cli.main import parse_params

def test_help_command():
    result = subprocess.run(["sentinel", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Usage" in result.stdout

def test_unknown_command():
    result = subprocess.run(["sentinel", "oops"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "No such command" in result.stderr or "Usage" in result.stdout

def test_parse_params_valid():
    params = ["user_id=123", "role=admin"]
    parsed = parse_params(params)
    assert parsed == {"user_id": "123", "role": "admin"}

def test_parse_params_invalid():
    with pytest.raises(ValueError) as exc:
        parse_params(["invalidparam"])
    assert "Invalid param format" in str(exc.value)
