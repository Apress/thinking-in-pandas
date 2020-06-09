import io

import pandas as pd
import numpy as np


data = io.StringIO(
"""
id,birth,height,weight
129237,04/10/1999,5.4,126
123083,07/03/2000,6.1,150
123087,11/23/1989,4.5,111
"""
)

df = pd.read_csv(
    data,
    dtype={"id": np.int32, "height": np.float16, "weight": np.int16},
    parse_dates=["birth"],
    index_col=[0],
)

print(df)
print(df.memory_usage(deep=True))
print(df.dtypes)
print(df.index.dtype)
