import pandas as pd
import numpy as np


df = pd.DataFrame(
    [["Diner", (4, 2), 90, 100], ["Pandas", (5, 4), 55, 76]],
    columns=["restaurant", "location", 0, 1],
)

print(df)
df = df.melt(
    id_vars=["restaurant", "location"], value_vars=[0, 1], value_name="score"
).drop(columns="variable")
print(df)
