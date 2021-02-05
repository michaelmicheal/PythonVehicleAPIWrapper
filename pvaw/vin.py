from . import session
from typing import Union, List, Tuple
from pvaw.vehicle import Vehicle
from pvaw.utils import get_path


class Vin:
    def __init__(self, full_or_partial_vin: str, year: Union[str, int] = None) -> None:
        if not isinstance(full_or_partial_vin, str):
            raise TypeError('"full_or_partial_vin" must be a str')

        if len(full_or_partial_vin) > 17:
            raise ValueError('"full_or_partial_vin" must be at most 17 characters')

        if year is not None:
            print(year)
            if not isinstance(year, (int, str)):
                raise TypeError('"year" must be a str or int')

            if int(year) < 1953:
                raise ValueError('"year" must be greater than 1953')

        self.full_or_partial_vin = full_or_partial_vin
        self.year = year

    def decode(self) -> Vehicle:
        if self.year is not None:
            after_format = f"&modelyear={self.year}"
        path = get_path("DecodeVinValues", self.full_or_partial_vin, after_format)
        response = session.get(path)
        results_dict = response.json()["Results"][0]

        return Vehicle(self.full_or_partial_vin, self.year, results_dict)