import pandas as pd


building_records_1844 = pd.DataFrame(
    [["Grande Hotel", 1832],
    ["Jone’s Farm", 1842],
    ["Public Library", 1836],
    ["Marietta House", 1823]],
    columns=["building", "established"],
)

building_records_2020 = pd.DataFrame(
    [["Sam’s Bakery", 1962],
    ["Grande Hotel", 1830],
    ["Public Library", 1836],
    ["Mayberry’s Factory", 1924]],
    columns=["building", "established"],
)


print(building_records_1844)

print(building_records_2020)

merged_records = pd.merge(
    building_records_2020,
    building_records_1844,
    how="left",
    right_on="building",
    left_on="building",
    suffixes=("_2000", ""),
)

print(merged_records)

merged_records["established"].fillna(merged_records["established_2000"], inplace=True)

del merged_records["established_2000"]

print(merged_records)
