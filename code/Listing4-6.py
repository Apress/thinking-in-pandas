import io

import pandas as pd


site1 = io.StringIO(
    """
site1
129237
123083
"""
)

site2 = io.StringIO(
    """
129337
123583
"""
)

site_data = pd.read_csv(site1)
site_data["site2"] = pd.read_csv(site2, squeeze=True, header=None)
print(site_data)
