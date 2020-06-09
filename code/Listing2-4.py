import pandas as pd

account_info = pd.DataFrame(
    {
        "name": ["Bob", "Mary", "Mita"],
        "account": [123846, 123972, 347209],
        "balance": [123, 3972, 7209],
    }
)

print(account_info.iloc[1, 2])

account_info.iloc[1, 2] = 3975

print(account_info.iloc[1, 2])
print(account_info.iloc[:, [0, 2]])
