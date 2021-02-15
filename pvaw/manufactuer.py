from __future__ import annotations
from typing import Dict, List, Union
import pandas as pd
from pvaw import session
from pvaw.constants import VEHICLE_API_PATH
from pvaw.results import Results, ResultsList


MANUFACTURER_TYPES = frozenset(
    {
        "Incomplete Vehicles",
        "Completed Vehicle Manufacturer",
        "Incomplete Vehicle Manufacturer",
        "Intermediate Vehicle Manufacturer",
        "Final-Stage Vehicle Manufacturer",
        "Vehicle Alterer",
        "Fabricating Manufacturer of Motor Vehicle Equipment",
        "Importer of Motor Vehicle Equipment",
        "Importer of Motor Vehicles Originally Manufactured to Conform to FMVSS",
        "Replica Vehicle Manufacturer",
    }
)


class Manufacturer(Results):
    def __init__(self, man_id: Union[str, int], results_dict: Dict[str, str]):
        super().__init__(man_id, results_dict)
        self.common_name = results_dict["Mfr_CommonName"]
        self.name = results_dict["Mfr_Name"]
        self.vehicle_types = [d["Name"] for d in results_dict["VehicleTypes"]]
        self.id = results_dict["Mfr_ID"]


def get_manufacturer_types() -> List[str]:
    return MANUFACTURER_TYPES


def get_manufacturers(m_type: str = None, page: int = 1) -> ResultsList:

    args = ["format=json"]
    if m_type is not None:
        if m_type not in MANUFACTURER_TYPES:
            raise ValueError(f"'{m_type}' is not a manufacturer type")
        args.append("ManufacturerType=Intermediate")

    if page is not None:
        if not isinstance(page, int):
            raise TypeError("'page' parameter must be an int")
        args.append(f"page={page}")

    args_str = "&".join(args)

    path = f"{VEHICLE_API_PATH}getallmanufacturers?{args_str}"

    response = session.get(path)
    results_list = response.json()["Results"]

    return ResultsList(
        [
            Manufacturer(results_dict["Mfr_ID"], results_dict)
            for results_dict in results_list
        ]
    )


def get_manufacturer_details(manufacturer_name_or_id: Union[str, int]) -> Manufacturer:

    if not isinstance(manufacturer_name_or_id, (str, int)):
        raise TypeError("'manufacturer_name_or_id' must be a str or int")

    path = f"{VEHICLE_API_PATH}GetManufacturerDetails/{manufacturer_name_or_id}?format=json"

    response = session.get(path)
    results_list = response.json()["Results"]

    return ResultsList(
        [
            Manufacturer(results_dict["Mfr_ID"], results_dict)
            for results_dict in results_list
        ]
    )
