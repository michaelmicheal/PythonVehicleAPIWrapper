from . import session
from typing import Union, List, Tuple
from pvaw.vehicle import Vehicle
from pvaw.constants import VEHICLE_API
class Vin:

    def __init__(self, full_or_partial_vin: str, year: Union[str, int]= None) -> None:
        self.full_or_partial_vin = full_or_partial_vin
        self.year = year
    

    def decode(self) -> Vehicle:
        path = f'{VEHICLE_API}DecodeVinValues/{self.full_or_partial_vin}?format=json'
        if self.year is not None:
            path += '&modelyear={year}'
        response = session.get(path)
        vehicle_dict = response.json()['Results'][0]
        return Vehicle(vehicle_dict)

    @classmethod
    def decode_vin_list(cls, vins: Union[Tuple[Tuple[str, Union[str, int]]]]) -> Tuple[Vehicle]:
        vehicle_list = []
        for el in vins:
            if isinstance(el, tuple):
                if len(el) == 1:
                    vin = Vin(el[0])
                elif len(el) == 2:
                    vin = Vin(el[0], el[1])
                else:
                    continue
            elif isinstance(el, str):
                vin = Vin(el)
            else:
                continue
            vehicle_list.append(vin)

        return vehicle_list

