import io

import pandas as pd


data = io.StringIO(
"""
{
    "temp": {
        "234unf923": 35.2,
        "340inf351": 32.5,
        "234abe045": 33.1,
    },
}
"""
)

print(pd.read_json(data, orient="columns"))
