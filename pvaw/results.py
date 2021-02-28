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

    def get_series(self):
        return pd.Series(self.results_dict).replace(
            to_replace=r"^\s*$", value=np.nan, regex=True
        )

    def get_df(self, drop_na: bool = True) -> pd.DataFrame:
        df = pd.DataFrame({self.identifier: self.get_series()})
        if drop_na:
            df.dropna(inplace=True)
        return df.T

    def get_attribute_strings(self):
        return (("identifer", self.identifier),)

    def __str__(self):
        attribute_str = "\n".join(
            ": ".join(str(el) for el in att) for att in self.get_attribute_strings()
        )
        return f"{self.__class__.__name__}:\n{attribute_str}"

    def _repr_html_(self):
        rows = "\n".join(
            "<tr>{0}</tr>".format("".join(f"<td>{el}</td>" for el in att))
            for att in self.get_attribute_strings()
        )
        header = "<tr><th>Attribute</th><th>Value</th></tr>"
        return f"{self.__class__.__name__}:<table>{header}{rows}</table>"


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
        vehicles_html = ",\n ".join(
            results._repr_html_() for results in self.results_list[: self.MAX_LIST]
        )
        if len(self) >= self.MAX_LIST:
            vehicles_html += ",\n..."
        return f"[{vehicles_html}]"

    def get_results(self) -> List[Dict[str, str]]:
        return [r.get_results() for r in self.results_list]

    def get_df(self, drop_na: bool = True):
        df = pd.DataFrame()
        for manu in self.results_list:
            df[manu.identifier] = manu.get_series()
        if drop_na:
            df.dropna(inplace=True)
        return df.T
