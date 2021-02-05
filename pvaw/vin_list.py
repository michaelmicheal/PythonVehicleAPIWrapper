from . import session
from typing import Union, List, Tuple
from pvaw.vehicle import Vehicle
from pvaw.vehicle_list import VehicleList
from pvaw.vin import Vin
from pvaw.utils import post_path, post_fields


class BatchVinDecodeError(Exception):
    pass


class VinList(Vin):
    def __init__(self, vins: Union[Tuple[Tuple[str, Union[str, int]]]]) -> None:
        self.vin_list = []
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
        self.vin_list.append(vin)

    def decode(self) -> List[Vehicle]:
        vin_batch_str = ";".join(
            vin.full_or_partial_vin
            if vin.year is None
            else f"{vin.full_or_partial_vin},{vin.year}"
            for vin in self.vin_list
        )
        path = post_path("DecodeVINValuesBatch")

        try:
            response = session.post(path, post_fields(vin_batch_str))
            results_list = response.json()["Results"]
        except ...:
            raise BatchVinDecodeError("Error in API request")

        if len(results_list) != len(self.vin_list):
            raise BatchVinDecodeError("Incorrect number of results returned from API")

        return VehicleList(
            [
                Vehicle(
                    self.vin_list[i].full_or_partial_vin, self.year, results_list[i]
                )
                for i in range(len(results_list))
            ]
        )
