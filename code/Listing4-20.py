import io

import pandas as pd


data = io.StringIO(
"""
{
"columns": ["temp"],
"index": ["234unf923", "340inf351", "234abe045"],
"data": [[35.2],[32.5],[33.1]],
}
"""
)

print(pd.read_json(data, orient="split"))
