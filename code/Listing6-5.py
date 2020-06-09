import pandas as pd
import numpy as np


df = pd.DataFrame({"A": [0, np.nan, np.nan, 4], "B": [0, 1, 2, 3], "C": [0, 4, 1, 5]})


def replace_missing(series):
    if np.isnan(series["A"]):
        series["A"] = max(series["B"], series["C"])
    return series


df = df.apply(replace_missing, axis=1)
