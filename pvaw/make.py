from __future__ import annotations
from typing import Dict, List, Union
import pandas as pd
import requests
from pvaw.constants import VEHICLE_API_PATH
from pvaw.results import Results, ResultsList
from pvaw.utils import check_model_year


class Make(Results):
    def __init__(self, results_dict: Dict[str, str]):
        if "Make_ID" in results_dict.keys():
            self.make_id = results_dict["Make_ID"]
        else:
            self.make_id = results_dict["MakeId"]

        if "Make_Name" in results_dict.keys():
            self.make_name = results_dict["Make_Name"]
        else:
            self.make_name = results_dict["MakeName"]

        if "Mfr_Name" in results_dict.keys():
            self.manufacturer = results_dict["Mfr_Name"]
        elif "MfrName" in results_dict.keys():
            self.manufacturer = results_dict["MfrName"]
        else:
            self.manufacturer = None

        if "VehicleTypeName" in results_dict.keys():
            self.vehicle_type = results_dict["VehicleTypeName"]
        else:
            self.vehicle_type = None

        super().__init__(f"{self.make_id}-{self.manufacturer}", results_dict)


def get_makes(
    manufacturer_name_or_id: Union[str, int] = None,
    model_year: Union[str, int] = None,
    vehicle_type: str = None,
) -> ResultsList:

    if manufacturer_name_or_id is not None and not isinstance(
        manufacturer_name_or_id, (str, int)
    ):
        raise TypeError("'manufacturer_name_or_id' must be a str or int")

    if model_year is not None:
        check_model_year(model_year)

    if vehicle_type is not None and not isinstance(vehicle_type, str):
        raise TypeError("'vehicle_type' must be a str")

    if vehicle_type is not None and (manufacturer_name_or_id is not None):
        raise ValueError(
            "Cannot filter by 'vehicle_type' and 'manufacturer_name_or_id'"
        )

    if manufacturer_name_or_id is None and model_year is not None:
        raise ValueError(
            "Cannot search by 'model_year' without 'manufacturer_name_or_id'"
        )

    if manufacturer_name_or_id is not None:
        if model_year is not None:
            path = f"{VEHICLE_API_PATH}GetMakesForManufacturerAndYear/{manufacturer_name_or_id}?year={model_year}&format=json"
        else:
            path = f"{VEHICLE_API_PATH}GetMakeForManufacturer/{manufacturer_name_or_id}?format=json"
    else:
        path = f"{VEHICLE_API_PATH}GetMakesForVehicleType/{vehicle_type}?format=json"

    response = requests.get(path)
    results_list = response.json()["Results"]

    return ResultsList([Make(results_dict) for results_dict in results_list])
