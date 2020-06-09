import pandas as pd
import numpy as np


df = (
    pd.DataFrame(
        [
            ["Diner", (4, 2), 0, 90],
            ["Pandas", (5, 4), 0, 55],
            ["Diner", (4, 2), 1, 100],
            ["Pandas", (5, 4), 1, 76],
        ],
        columns=["restaurant", "location", "inspection", "score"],
    )
    .set_index(["restaurant", "location", "inspection"])
    .unstack()
)

print(df)
df = df.stack().reset_index()
print(df)
df.drop(columns=["inspection"], inplace=True)
df.set_index(["restaurant", "location"], inplace=True)
print(df)
