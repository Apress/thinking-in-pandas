import io

import pandas as pd


data = io.StringIO(
    """
id,age,height,weight
129237,32,5.4,126
123083,20,6.1,145
"""
)

df = pd.read_csv(data, index_col=[0])

print(df)
print(df.memory_usage(deep=True))
print(df.dtypes)
print(df.index.dtype)
