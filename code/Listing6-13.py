import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(20).reshape(4, 5))


def percentileofscore(df):

    res_df = pd.DataFrame({})

    for col in df.columns:

        score = pd.DataFrame([df[col]] * 5, index=df.columns).T

    left = df[df < score].count(axis=1)

    right = df[df <= score].count(axis=1)

    right_is_greater = (
        df[df <= score].count(axis=1) > df[df < score].count(axis=1)
    ).astype(int)

    res_df[f"res{col}"] = (left + right + right_is_greater) * 50.0 / len(df.columns)

    return res_df


percentileofscore(data)
