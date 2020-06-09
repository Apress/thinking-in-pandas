import io

import pandas as pd
import numpy as np


data = io.StringIO(
"""
{
    "birth": {
        "129237": "04/10/1999",
        "123083": "05/18/1989",
    },
    "height": {
        "129237": 5.4,
        "123083": 6.1,
    },
    "weight": {
        "129237": 126,
        "123083": 130,
    },
}
"""
)

patient_info = pd.read_json(
    data,
    orient="columns",
    convert_dates=["birth"],
    dtype={"height": np.float16, "weight": np.int16},
)

print(patient_info)
print(patient_info.dtypes)
print(patient_info.index.dtype)
print(patient_info.memory_usage())
