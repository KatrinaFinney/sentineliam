import pytest
import tempfile
from engine.validator import validate_policy
from pathlib import Path

def test_valid_policy():
    valid_yaml = '''
    version: "2025-03-26"
    statement:
      - effect: "allow"
        action: "read"
        resource: "db"
    '''
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(valid_yaml)
        temp_path = f.name

    doc = validate_policy(temp_path)
    assert doc.version == "2025-03-26"
    Path(temp_path).unlink()

def test_invalid_yaml():
    invalid_yaml = '''not: yaml: - here'''
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(invalid_yaml)
        temp_path = f.name

    with pytest.raises(ValueError) as e:
        validate_policy(temp_path)
    assert "Invalid policy" in str(e.value)
    Path(temp_path).unlink()

def test_missing_fields():
    missing = '''
    statement:
      - action: "read"
        resource: "db"
    '''
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(missing)
        temp_path = f.name

    with pytest.raises(ValueError):
        validate_policy(temp_path)
    Path(temp_path).unlink()