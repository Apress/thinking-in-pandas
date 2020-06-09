import pandas as pd

account_info = pd.DataFrame(
    {
        "name": ["Bob", "Mary", "Mita"],
        "account": [123846, 123972, 347209],
        "balance": [123, 3972, 7209],
    }
)

print(account_info["name"])

account_info["name"] = ["Smith", "Jane", "Patel"]

print(account_info)
