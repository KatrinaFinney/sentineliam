import yaml
from .models import PolicyDocument

def validate_policy(file_path: str) -> PolicyDocument:
    try:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
        return PolicyDocument(**data)
    except Exception as e:
        raise ValueError(f"Invalid policy: {e}")
