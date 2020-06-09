import pandas as pd

import numpy as np

import numexpr as ne


nrows, ncols = 200000, 1

df1, df2, df3, df4 = [pd.DataFrame(np.random.randn(nrows, ncols)) for _ in range(4)]


# Calculate the sum using normal syntax.

df_sum1 = df1 + df2 + df3 + df4


# Calculate the sum using eval so that NumExpr optimizes it.

df_sum2 = pd.eval(" df1 + df2 + df3 + df4")


# Calculate the sum using NumExpr directly.

a1, a2, a3, a4 = (df1.to_numpy(), df2.to_numpy(), df3.to_numpy(), df4.to_numpy())

df_sum3 = ne.evaluate("a1 + a2 + a3 + a4")
