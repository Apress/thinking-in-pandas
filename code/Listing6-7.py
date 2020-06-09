import pandas as pd
import numpy as np


def test_fruit_in_order(series):
    if series["fruit"].lower() in series["order"].lower():
        return series
    return np.nan


data = pd.DataFrame(
    {
        "fruit": ["orange", "lemon", "mango"],
        "order": ["I'd like an orange", "Mango please.", "May I have a mango?"],
    }
)

print(data)
print(data.apply(test_fruit_in_order, axis=1, result_type="reduce").dropna())
