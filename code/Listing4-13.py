import io

import pandas as pd


data = io.StringIO(
"""
student_id, grade
1045,"a"
2391,"b"
,"c"
1092,"a"
"""
)

grades = pd.read_csv(
    data, verbose=True, index_col="student_id", engine="python"
)
print(grades)
print(grades.index.dtype)
