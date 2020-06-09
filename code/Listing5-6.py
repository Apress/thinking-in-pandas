import pandas as pd
import numpy as np


df = pd.DataFrame(
    [
        ["Diner", (4, 2), 90],
        ["Pandas", (5, 4), 55],
        ["Diner", (4, 2), 100],
        ["Pandas", (5, 4), 76],
    ],
    columns=["restaurant", "location", "score"],
).set_index(["restaurant", "location"])

print(df)
df["inspection"] = df.groupby(["restaurant", "location"]).cumcount()
df.set_index("inspection", append=True, inplace=True)

print(df)
df = df.unstack()
print(df)
