from typing import Dict, Any
from pvaw.constants import VEHICLE_API_PATH


def value_or_none(dict: Dict[str, str], key: str) -> str:
    val = dict[key]
    if isinstance(val, str) and not val.strip():
        return None
    return val


def get_path(api: str, before_format: str = None, after_format: str = None) -> str:
    return f"{VEHICLE_API_PATH}{api}/{before_format}?format=json"


def post_path(api: str) -> str:
    return f"{VEHICLE_API_PATH}{api}/"


def post_fields(data: Any) -> Dict:
    return {"format": "json", "data": data}