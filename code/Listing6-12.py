import pandas as pd
import numpy as np
from scipy import stats

data = pd.DataFrame(np.arange(20).reshape(4, 5))

print(data)


def apply_percentileofscore(series):

    return series.apply(lambda x: stats.percentileofscore(series, x))


print(data.apply(apply_percentileofscore, axis=1))
