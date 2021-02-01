from . import session
from typing import Union, List, Tuple
from pvaw.vehicle import Vehicle
from pvaw.vin import Vin
from pvaw.constants import VEHICLE_API

class BatchVinDecodeError(Exception):
    pass


class VinList(Vin):

    def __init__(self, vins: Union[Tuple[Tuple[str, Union[str, int]]]]) -> None:
        vin_list = []
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
            vin_list.append(vin)
        self.vin_list = vin_list
        
    

    def decode(self) -> List[Vehicle]:
        vin_batch = ''
        for vin in self.vin_list:
            if len(vin_batch) > 0:
                vin_batch += ';'
            vin_batch += vin.full_or_partial_vin
            if vin.year is not None:
                vin_batch += f', {vin.year}'
        path = f'{VEHICLE_API}DecodeVINValuesBatch/'
        post_fields = {'format': 'json', 'data': vin_batch}

        try:
            response = session.post(path, post_fields)
            results_list = response.json()['Results']
        except ...:
            raise BatchVinDecodeError
        
        vehiclelist = [Vehicle(results_dict) for results_dict in results_list]
        return vehiclelist


