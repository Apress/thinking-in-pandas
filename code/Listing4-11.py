import io

import pandas as pd


data_csv = io.StringIO(
"""
student_id, grade
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
    data_csv.seek(0)
    return data

ROWS_PER_CHUNK = 1000

data = process(pd.read_csv(data_csv, nrows=ROWS_PER_CHUNK))
read_rows = len(data)

chunk = 1
while chunk * ROWS_PER_CHUNK == read_rows:
    chunk_data = process(
        pd.read_csv(
            data_csv,
            skiprows=chunk * ROWS_PER_CHUNK,
            nrows=ROWS_PER_CHUNK,
            header=None,
            names=data.columns,
        )
    )
    read_rows += len(chunk_data)
    data = data.append(process(chunk_data), ignore_index=True)
