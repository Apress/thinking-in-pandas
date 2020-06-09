import io

import pandas as pd
import numpy as np


data = io.StringIO(
"""
id,age,height,weight
129237,32,5.4,126
123083,20,6.1,
123087,25,4.5,unknown
"""
)

df = pd.read_csv(data, dtype={"id": np.int32, "age": np.int8, "height": np.float16}, index_col=[0])

print(df)
print(df.memory_usage(deep=True))
print(df.dtypes)
print(df.index.dtype)
