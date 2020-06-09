import pandas as pd


df = pd.DataFrame({"a": [0, 1, 2, 3], "b": [0, 1, 2, 3]})

results = [0] * len(df)
for i, v in df.iterrows():
    results[i] = v.sum()
df["sum"] = results
print(df)
