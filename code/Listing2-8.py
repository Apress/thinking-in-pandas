import pandas as pd
import numpy as np


customers = pd.MultiIndex.from_tuples(
    (("Bob", "smithb"), ("Mary", "mj100"), ("Mita", "patelm")),
    names=["name", "username"],
)

accounts = pd.MultiIndex.from_tuples(
    ((0, "number"), (0, "balance"), (1, "number"), (1, "balance")), names=["account", "account_info"]
)

account_info = pd.DataFrame(
    [[123846, 123, 123847, 450], [123972, 3972, 123973, 222], [347209, 7209, np.nan, np.nan]],
    index=customers,
    columns=accounts,
)

print(account_info)

print(account_info.loc[("Mary", "mj100"), pd.IndexSlice[:, "balance"]])
