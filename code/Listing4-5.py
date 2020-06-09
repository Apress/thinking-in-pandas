import io

import pandas as pd


data = io.StringIO(
    """
family,,nightshade,nightshade,nightshade
species,,tomatoe,deadly-nightshade,potato
family_id,species_id,,,
61248,129237,1,0,0
61248,123083,0,1,0
61248,123729,0,0,1
"""
)

print(pd.read_csv(data, header=[0, 1], index_col=[0, 1]))
