from . import session
from typing import Dict, List
import pandas as pd
import numpy as np
from pvaw.results import Results, ResultsList
from pvaw.utils import get_path
from pvaw.constants import VEHICLE_API_PATH


class WMI(Results):
    def __init__(self, results_dict: Dict[str, str]) -> None:
        super().__init__(results_dict["WMI"], results_dict)
        self.wmi = results_dict["WMI"]
        self.vehicle_type = results_dict["VehicleType"]
        if "ManufacturerName" in results_dict.keys():
            self.manufacturer_name = results_dict["ManufacturerName"]
        else:
            self.manufacturer_name = results_dict["Name"]


def decode_wmi(wmi: str) -> WMI:
    if not isinstance(wmi, str):
        raise TypeError("'wmi' must be a str")
    if not len(wmi) in (3, 6):
        raise ValueError(
            "'wmi' must be length 3 representing VIN position 1-3 "
            "or length 6 representing VIN positions 1-3 & 12-14."
        )

    path = f"{VEHICLE_API_PATH}DecodeWMI/{wmi}?format=json"
    response = session.get(path)
    results_dict = response.json()["Results"][0]
    results_dict["WMI"] = wmi
    return WMI(results_dict)


def get_manufacturer_wmis(make_search: str) -> List[WMI]:
    if not isinstance(make_search, str):
        raise TypeError("'make_search' must be a str")

    path = f"{VEHICLE_API_PATH}GetWMIsForManufacturer/{make_search}?format=json"
    response = session.get(path)
    results = response.json()["Results"]
    return ResultsList([WMI(result) for result in results])
