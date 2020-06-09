import io

import pandas as pd


data = io.StringIO(
"""
id| age| height| weight
129237| 32| 5.4| 126
123083| 20| 6.1| 145
"""
)

print(pd.read_csv(data, sep="|", skipinitialspace=True))
