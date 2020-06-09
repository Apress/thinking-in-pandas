import pandas as pd
import numpy as np


data = pd.DataFrame({"size": [np.nan, 1.0, 3.5]})
print(data.dtypes)
print(id(data._data.blocks[0].values))

data.fillna(0.0, inplace=True)
print(data.dtypes)
print(id(data._data.blocks[0].values))

data.replace(0.0, "null", inplace=True)
print(data.dtypes)
print(id(data._data.blocks[0].values))
