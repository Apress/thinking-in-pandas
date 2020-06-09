import pandas as pd
import numpy as np


df = pd.DataFrame([[4, 9], [6, 7]], columns=["A", "B"])
print(df)
print(df.apply(np.sum, axis=1))
