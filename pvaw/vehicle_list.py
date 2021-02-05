from __future__ import annotations
import pandas as pd
from pvaw.vehicle import Vehicle
from typing import List


class VehicleList(Vehicle):
    def __init__(self, vehicle_list: List[Vehicle]) -> None:
        self.vehicle_list = vehicle_list
        self.index = 0

    def __iter__(self) -> VehicleList:
        return self

    def __next__(self) -> Vehicle:
        if self.index < len(self.vehicle_list):
            current = self.vehicle_list[self.index]
            self.index += 1
            return current
        else:
            raise StopIteration

    def get_df(self, drop_na: bool = False):
        df = pd.DataFrame()
        for vehicle in self.vehicle_list:
            df[vehicle.search_name()] = vehicle.get_series()
        if drop_na:
            df.dropna(inplace=True)
        return df.T
