from typing import Dict, Any, Union
from pvaw.constants import VEHICLE_API_PATH, EARLIEST_YEAR


def get_int(num: Union[int, str]) -> int:
    try:
        return int(num)
    except ...:
        return None


def check_model_year(model_year: Union[str, int]) -> None:
    if not isinstance(model_year, (int, str)):
        raise TypeError("'model_year' must be a str or int")

    if int(model_year) < EARLIEST_YEAR:
        raise ValueError("'model_year' must be greater than 1953")