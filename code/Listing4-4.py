import io

import pandas as pd


data = io.StringIO(
    """
student_id, grade
1045,"a"
2391,"b"
8723,"c"
1092,"a'
"""
)

try:
    grades = pd.read_csv(data, skipfooter=1)
except pd.errors.ParserError as e:
    pass
