from __future__ import annotations
from typing import Dict, Any, List
import pandas as pd
import numpy as np


class Results:
    CLASS_NAME = "Results"

    def __init__(self, identifier: str, results_dict: Dict[str, Any]):
        self.identifier = identifier
        self.results_dict = results_dict

    def get_results(self) -> Dict[str, str]:
        return self.results_dict

    def get_key_attributes(self):
        d = self.__dict__.copy()
        d.pop("identifier", None)
        d.pop("results_dict", None)
        return d

    def get_series(self, raw):
        if raw:
            d = self.results_dict
        else:
            d = self.get_key_attributes()
        return pd.Series(d).replace(to_replace=r"^\s*$", value=np.nan, regex=True)

    def get_df(self, raw: bool = False, drop_na: bool = True) -> pd.DataFrame:
        df = pd.DataFrame({self.identifier: self.get_series(raw)})
        if drop_na:
            df.dropna(inplace=True)
        return df.T

    def __str__(self):
        d = self.get_key_attributes()
        attribute_str = "\n".join(": ".join(str(el) for el in att) for att in d.items())
        return f"{self.__class__.__name__}:\n{attribute_str}"

    def _repr_html_(self):
        return self.get_df(raw=False)._repr_html_()


class ResultsList:
    MAX_LIST = 5

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

    def __len__(self):
        return len(self.results_list)

    def __getitem__(self, index: int):
        return self.results_list[index]

    def __str__(self):
        vehicles_str = ",\n ".join(
            str(results) for results in self.results_list[: self.MAX_LIST]
        )
        if len(self) >= self.MAX_LIST:
            vehicles_str += ",\n..."
        return f"[{vehicles_str}]"

    def _repr_html_(self):
        return self.get_df(raw=False)._repr_html_()

    def get_results(self) -> List[Dict[str, str]]:
        return [r.get_results() for r in self.results_list]

    def get_df(self, raw: bool = False, drop_na: bool = True):
        df = pd.DataFrame()
        for rl in self.results_list:
            df[rl.identifier] = rl.get_series(raw=raw)
        if drop_na:
            df.dropna(inplace=True)
        return df.T
