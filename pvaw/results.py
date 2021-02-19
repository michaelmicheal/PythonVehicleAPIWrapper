from __future__ import annotations
from typing import Dict, Any, List
import pandas as pd
import numpy as np


class Results:
    def __init__(self, identifier: str, results_dict: Dict[str, Any]):
        self.identifier = identifier
        self.results_dict = results_dict

    def get_results(self) -> Dict[str, str]:
        return self.results_dict

    def get_series(self):
        return pd.Series(self.results_dict).replace(
            to_replace=r"^\s*$", value=np.nan, regex=True
        )

    def get_df(self, drop_na: bool = True) -> pd.DataFrame:
        df = pd.DataFrame({self.identifier: self.get_series()})
        if drop_na:
            df.dropna(inplace=True)
        return df.T


class ResultsList:
    def __init__(self, results_list: List[Results]):
        self.results_list = results_list
        self.index = 0

    def __iter__(self) -> ResultsList:
        return self

    def __next__(self) -> Results:
        if self.index < len(self.results_list):
            current = self.results_list[self.index]
            self.index += 1
            return current
        else:
            self.index = 0
            raise StopIteration

    def __getitem__(self, index: int):
        return self.results_list[index]

    def get_results(self) -> List[Dict[str, str]]:
        return [r.get_results() for r in self.results_list]

    def get_df(self, drop_na: bool = True):
        df = pd.DataFrame()
        for manu in self.results_list:
            df[manu.identifier] = manu.get_series()
        if drop_na:
            df.dropna(inplace=True)
        return df.T
