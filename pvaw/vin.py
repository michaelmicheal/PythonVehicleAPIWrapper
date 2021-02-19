from __future__ import annotations
from typing import Dict, Union, Tuple, List
import pandas as pd
import numpy as np
from pvaw.results import Results, ResultsList
from pvaw.utils import get_int, check_model_year
from pvaw.constants import VEHICLE_API_PATH
import requests


class BatchVinDecodeError(Exception):
    pass


class Vin:
    def __init__(self, full_or_partial_vin: str, model_year: Union[str, int] = None):
        if not isinstance(full_or_partial_vin, str):
            raise TypeError('"full_or_partial_vin" must be a str')

        if len(full_or_partial_vin) > 17:
            raise ValueError('"full_or_partial_vin" must be at most 17 characters')

        self.full_or_partial_vin = full_or_partial_vin

        if model_year is not None:
            check_model_year(model_year)
            self.model_year = int(model_year)
        else:
            self.model_year = None

    def __str__(self):
        if self.model_year is not None:
            return f"{self.full_or_partial_vin},{str(self.model_year)}"
        else:
            return self.full_or_partial_vin

    def decode(self) -> Vehicle:

        args = ["format=json"]
        if self.model_year is not None:
            args.append(f"modelyear={self.model_year}")

        args_str = "&".join(args)

        path = (
            f"{VEHICLE_API_PATH}DecodeVinValues/{self.full_or_partial_vin}?{args_str}"
        )

        response = requests.get(path)
        results_dict = response.json()["Results"][0]

        return Vehicle(self, results_dict)


def decode_vins(vin_list: List[Vin]) -> ResultsList:

    if not isinstance(vin_list, list) or any(not isinstance(v, Vin) for v in vin_list):
        raise TypeError("'vin_list' must be list of Vin objects")

    if len(vin_list) == 0:
        raise ValueError("'vin_list' must have at least on Vin")

    vin_batch_str = ";".join(str(vin) for vin in vin_list)

    path = f"{VEHICLE_API_PATH}DecodeVINValuesBatch/"

    post_fields = {"format": "json", "data": vin_batch_str}

    try:
        response = requests.post(path, post_fields)
        results_list = response.json()["Results"]
    except Exception:
        raise BatchVinDecodeError("Error in API request")

    if len(results_list) != len(vin_list):
        raise BatchVinDecodeError("Incorrect number of results returned from API")

    return ResultsList(
        [Vehicle(vin_list[i], results_list[i]) for i in range(len(results_list))]
    )


class Vehicle(Results):
    def __init__(
        self,
        vin: Vin,
        results_dict: Dict[str, str],
    ):
        super().__init__(str(vin), results_dict)

        self.model_year = get_int(results_dict["ModelYear"])
        self.make = results_dict["Make"]
        self.manufacturer = results_dict["Manufacturer"]
        self.model = results_dict["Model"]
        self.full_or_partial_vin = results_dict["VIN"]
        self.vehicle_type = results_dict["VehicleType"]
