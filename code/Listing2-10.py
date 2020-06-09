import pandas as pd


building_records_1844 = pd.DataFrame(
    [["Grande Hotel", 1830],
    ["Jone’s Farm", 1842],
    ["Public Library", 1836],
    ["Marietta House", 1823]],
    columns=["building", "established"],
).set_index(["building"])

building_records_2020 = pd.DataFrame(
    [["Sam’s Bakery", 1962],
    ["Grande Hotel", 1830],
    ["Public Library", 1836],
    ["Mayberry’s Factory", 1924]],
    columns=["building", "established"],
).set_index(["building"])

print(building_records_1844)

print(building_records_2020)
cols = building_records_2020.columns.difference(building_records_1844.columns)
print(
    pd.merge(building_records_1844, building_records_2020[cols], how="inner", on=["building"])
)
