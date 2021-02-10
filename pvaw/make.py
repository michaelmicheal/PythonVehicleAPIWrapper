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


class Make(Results):
    def __init__(
        self, manufacturer_name_or_id: Union[str, int], results_dict: Dict[str, str]
    ):
        super().__init__(manufacturer_name_or_id, results_dict)
        self.manufacturer_name_or_id = manufacturer_name_or_id
        self.make_id = results_dict["MakeId"]
        self.make_name = results_dict["MakeName"]
        self.vehicle_type = results_dict["VehicleTypeName"]

    def get_df(self, drop_na: bool = False) -> pd.DataFrame:
        df = pd.DataFrame({self.manufacturer_name_or_id: self.get_series()})
        if drop_na:
            df.dropna(inplace=True)
        return df.T


# TODO: move all attribute names to snake case


def get_makes(
    manufacturer_name_or_id: Union[str, int] = None,
    year: Union[str, int] = None,
    vehicle_type: str = None,
) -> ResultsList:

    if manufacturer_name_or_id is not None and not isinstance(
        manufacturer_name_or_id, (str, int)
    ):
        raise TypeError("'manufacturer_name_or_id' must be a str or int")

    if year is not None and not isinstance(year, (str, int)):
        raise TypeError("'year' must be a str or int")

    if vehicle_type is not None and not isinstance(vehicle_type, str):
        raise TypeError("'vehicle_type' must be a str")

    if vehicle_type is not None and (manufacturer_name_or_id is not None):
        raise ValueError(
            "Cannot filter by 'vehicle_type' and 'manufacturer_name_or_id'"
        )
    if vehicle_type is not None and (year is not None):
        raise ValueError("Cannot filter by 'vehicle_type' and 'year'")

    if manufacturer_name_or_id is None and year is not None:
        raise ValueError("Cannot search by 'year' without 'manufacturer_name_or_id'")

    ## TODO: add check_year method

    if manufacturer_name_or_id is not None:
        if year is not None:
            path = f"{VEHICLE_API_PATH}GetMakesForManufacturerAndYear/{manufacturer_name_or_id}?year={year}&format=json"
        else:
            path = f"{VEHICLE_API_PATH}GetMakesForManufacturer/{manufacturer_name_or_id}?format=json"
    else:
        path = f"{VEHICLE_API_PATH}GetMakesForVehicleType/{vehicle_type}?format=json"

    response = session.get(path)
    results_list = response.json()["Results"]

    return ResultsList(
        [Make(results_dict["MakeId"], results_dict) for results_dict in results_list]
    )

    # TODO: look into kwargs vs args good style in libraries
