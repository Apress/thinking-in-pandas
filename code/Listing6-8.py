import pandas as pd
import numpy as np


data = pd.DataFrame(
    {
        "fruit": ["orange", "lemon", "mango"],
        "order": ["I'd like an orange", "Mango please.", "May I have a mango?"],
    }
)

mask = [
    fruit.lower() in order.lower() for (fruit, order) in data[["fruit", "order"]].values
]
data = data[mask]
