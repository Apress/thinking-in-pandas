import io

import pandas as pd
import numpy as np


data = io.StringIO(
    """
id,name
129237,Mary
123083,Lacey
123087,Bob
"""
)

dtype = {"id": np.int32}
if pd.__version__ >= "1.0.0":
    dtype = {"id": np.int32, "name": pd.StringDtype()}


df = pd.read_csv(data, dtype=dtype, index_col=[0])
print(df)
print(df.memory_usage(deep=True))
print(df.dtypes)
