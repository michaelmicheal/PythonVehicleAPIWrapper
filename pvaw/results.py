from typing import Dict, Any, List
import pandas as pd
import numpy as np


class Results:
    def __init__(self, results_dict: Dict[str, Any]):
        self.results_dict = results_dict

    def get_dict(self) -> Dict[str, str]:
        return self.results_dict

    def get_series(self):
        return pd.Series(self.results_dict).replace(
            to_replace=r"^\s*$", value=np.nan, regex=True
        )


# class ResultsList:
#     def __init__(self, results_list: List[Results]):
#         self.results_list = results_list
