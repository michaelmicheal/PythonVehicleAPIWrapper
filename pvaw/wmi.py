from . import session
from typing import Dict, List
import pandas as pd
import numpy as np
from pvaw.results import Results
from pvaw.utils import get_path


class WMI(Results):
    def __init__(self, results_dict: Dict[str, str]) -> None:
        super().__init__(results_dict)
        self.wmi = results_dict["WMI"]
        self.CreatedOn = results_dict["CreatedOn"]
        self.DateAvailableToPublic = results_dict["DateAvailableToPublic"]
        self.ManufacturerName = results_dict["ManufacturerName"]
        self.UpdatedOn = results_dict["UpdatedOn"]
        self.VehicleType = results_dict["VehicleType"]


class WMIInfo(WMI):
    def __init__(self, results_dict: Dict[str, str]) -> None:
        self.results_dict = results_dict
        self.wmi = results_dict["WMI"]
        self.CreatedOn = results_dict["CreatedOn"]
        self.DateAvailableToPublic = results_dict["DateAvailableToPublic"]
        self.ManufacturerName = results_dict["ManufacturerName"]
        self.UpdatedOn = results_dict["UpdatedOn"]
        self.VehicleType = results_dict["VehicleType"]
        self.CommonName = results_dict["CommonName"]
        self.Make = results_dict["Make"]
        self.ParentCompanyName = results_dict["ParentCompanyName"]
        self.URL = results_dict["URL"]


class WMISearchResult(WMI):
    def __init__(self, results_dict: Dict[str, str]) -> None:
        self.results_dict = results_dict
        self.wmi = results_dict["WMI"]
        self.CreatedOn = results_dict["CreatedOn"]
        self.DateAvailableToPublic = results_dict["DateAvailableToPublic"]
        self.ManufacturerName = results_dict["Name"]
        self.UpdatedOn = results_dict["UpdatedOn"]
        self.VehicleType = results_dict["VehicleType"]
        self.Country = results_dict["Country"]


class WMISearchResults:
    def __init__(self, wsr_list: List[WMISearchResult]):
        self.wsr_list = wsr_list

    def get_dict(self, drop_na: bool = True):
        df = pd.DataFrame()
        for wsr in self.wsr_list:
            df[wsr.wmi] = wsr.get_series()
        if drop_na:
            df.dropna(inplace=True)
        return df.T


def decode_wmi(wmi: str) -> WMI:
    if not isinstance(wmi, str):
        raise TypeError("'wmi' must be a str")
    if not len(wmi) in (3, 6):
        raise ValueError(
            "'wmi' must be length 3 representing VIN position 1-3 "
            "or length 6 representing VIN positions 1-3 & 12-14."
        )

    path = get_path("DecodeWMI", wmi)
    response = session.get(path)
    results_dict = response.json()["Results"][0]
    results_dict["WMI"] = wmi
    return WMIInfo(results_dict)


def get_manufacturer_wmis(make_search: str) -> List[WMI]:
    if not isinstance(make_search, str):
        raise TypeError("'make_search' must be a str")

    path = get_path("GetWMIsForManufacturer", make_search)
    response = session.get(path)
    results = response.json()["Results"]
    return WMISearchResults([WMISearchResult(result) for result in results])


## TODO: Add getpath util function
