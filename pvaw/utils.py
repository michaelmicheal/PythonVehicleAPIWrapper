from typing import Dict, Any, Union
from pvaw.constants import VEHICLE_API_PATH


def get_int(num: Union[int, str]) -> int:
    try:
        return int(num)
    except ...:
        return None
