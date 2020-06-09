import pandas as pd
import numpy as np


df = pd.DataFrame(
    [
        ["Diner", (4, 2), "02/18", 90],
        ["Pandas", (5, 4), "04/18", 55],
        ["Diner", (4, 2), "05/18", 100],
        ["Pandas", (5, 4), "01/18", 76],
    ],
    columns=["restaurant", "location", "date", "score"],
)

print(df)
df = df.pivot_table(values=["score"], index=["restaurant", "location"], aggfunc=np.mean)
print(df)
