import io

import pandas as pd


MEDICATIONS_MAPPER = {"atg": "atg", "aftg": "atg", "bta": "bta"}


def medication_converter(value):
    return MEDICATIONS_MAPPER[value.lower()]


data = io.StringIO(
"""
id,age,height,weight,med
129237,32,5.4,126,bta
123083,20,6.1,145,aftg
"""
)

print(pd.read_csv(data, converters={"med": medication_converter}))
