from __future__ import annotations
from typing import Dict, Union, Tuple, List
import pandas as pd
import numpy as np
from pvaw.utils import value_or_none
from pvaw.results import Results, ResultsList
from pvaw.utils import get_path, post_path, post_fields
from pvaw.constants import VEHICLE_API_PATH
from pvaw import session


class BatchVinDecodeError(Exception):
    pass


def decode_vin(full_or_partial_vin: str, year: Union[str, int] = None) -> Vehicle:

    if not isinstance(full_or_partial_vin, str):
        raise TypeError('"full_or_partial_vin" must be a str')

    if len(full_or_partial_vin) > 17:
        raise ValueError('"full_or_partial_vin" must be at most 17 characters')

    args = ["format=json"]

    if year is not None:
        if not isinstance(year, (int, str)):
            raise TypeError('"year" must be a str or int')

        if int(year) < 1953:
            raise ValueError('"year" must be greater than 1953')

        args.append(f"modelyear={year}")

    args_str = "&".join(args)

    path = f"{VEHICLE_API_PATH}DecodeVinValues/{full_or_partial_vin}?{args_str}"

    response = session.get(path)
    results_dict = response.json()["Results"][0]

    return Vehicle(
        (
            full_or_partial_vin,
            year,
        ),
        results_dict,
    )


def decode_vins(vins: Union[Tuple[Tuple[str, Union[str, int]]]]) -> ResultsList:

    try:
        vin_batch_str = ";".join(",".join(str(el) for el in vin) for vin in vins)
    except ...:
        raise TypeError(
            "'vins' must be a tuple of vin tuples where each vin is represented as (vin, year)"
        )

    path = post_path("DecodeVINValuesBatch")

    try:
        response = session.post(path, post_fields(vin_batch_str))
        results_list = response.json()["Results"]
    except ...:
        raise BatchVinDecodeError("Error in API request")

    if len(results_list) != len(vins):
        raise BatchVinDecodeError("Incorrect number of results returned from API")

    return ResultsList(
        [Vehicle(vins[i], results_list[i]) for i in range(len(results_list))]
    )


class Vehicle(Results):
    def __init__(
        self,
        vin_search: Tuple[str, Union[str, int]],
        results_dict: Dict[str, str],
    ):
        super().__init__("".join(str(el) for el in vin_search), results_dict)

        if len(vin_search) == 2:
            self.model_year = vin_search[1]
        else:
            self.model_year = results_dict["ModelYear"]
        self.make = results_dict["Make"]
        self.manufacturer = results_dict["Manufacturer"]
        self.model = results_dict["Model"]
        self.full_or_partial_vin = results_dict["VIN"]
        self.vehicle_type = results_dict["VehicleType"]
