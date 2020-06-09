import io

import pandas as pd


data_csv = io.StringIO(
"""
student_id,grade
1045,"a"
2391,"b"
8723,"c"
1092,"a"
1045,"a"
2391,"b"
8723,"c"
1092,"a"
1045,"a"
2391,"b"
8723,"c"
1092,"a"
1045,"a"
2391,"b"
8723,"c"
1092,"a"
"""
)

def process(data):
    """ Mocked process function. """
    return data

ROWS_PER_CHUNK = 1000

data = pd.DataFrame({})

reader = pd.read_csv(data_csv, chunksize=ROWS_PER_CHUNK, iterator=True)

for data_chunk in reader:
    processed_data_chunk = process(data_chunk)
    data = data.append(processed_data_chunk)
