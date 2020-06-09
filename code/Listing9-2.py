import pandas as pd
import numpy as np


print(pd.Categorical([1, 3, 5, np.nan], ordered=True).min())
