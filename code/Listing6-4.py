import pandas as pd


df = pd.DataFrame({"a": [0, 1, 2, 3], "b": [0, 1, 2, 3]})

df.sum(axis=1)
