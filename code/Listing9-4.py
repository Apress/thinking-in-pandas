import pandas as pd


metadata = pd.Categorical(["Mary"] * 100000 + ["Boby"] * 100000 + ["Joe"] * 100000)

metadata.searchsorted(["Mary", "Joe"])
