import pandas as pd
import numpy as np


df = pd.DataFrame({"A": [0, np.nan, np.nan, 4], "B": [0, 1, 2, 3], "C": [0, 4, 1, 5]})

df["A"].where(~df["A"].isna(), df[["B", "C"]].max(axis=1), inplace=True)
