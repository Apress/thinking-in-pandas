import io

import pandas as pd


data = io.StringIO(
"""
temp,location
35,234unf923
32,2340inf012
33,2340inf351
33\,1,2340abe045
"""
)

print(pd.read_csv(data, decimal=",", escapechar="\\", index_col="location"))
