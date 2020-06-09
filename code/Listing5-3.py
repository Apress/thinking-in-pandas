import pandas as pd
import numpy as np


df = pd.DataFrame(
    [
        ["02/18", 90, 1384, 10],
        ["02/25", 80, 1384, 10],
        ["03/07", 65, 1384, 10],
        ["03/21", 60, 1384, 10],
        ["02/18", 30, 1389, 7],
        ["02/25", 20, 1389, 7],
        ["03/07", 25, 1389, 7],
        ["03/21", 25, 1389, 7],
    ],
    columns=["date", "tumor_size", "drug", "dose"],
)

print(df)
print(df.pivot(index="drug", columns="date", values="tumor_size"))
