import io

import pandas as pd


data = io.StringIO(
"""
{"location": "234unf923", "temp": 35.2}
{"location": "340inf351", "temp": 32.5}
{"location": "234abe045", "temp": 33.1}
"""
)

def process(data):
    """ Mocked process function. """
    return data

temperatures = pd.DataFrame({})

reader = pd.read_json(data, lines=True, chunksize=2)
for chunk in reader:
    temperatures = temperatures.append(process(chunk))

print(temperatures)
