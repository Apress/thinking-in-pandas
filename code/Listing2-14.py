import pandas as pd


building_records_1844 = pd.DataFrame(
    [["Grande Hotel", 1831],
    ["Jone’s Farm", 1842],
    ["Public Library", 1836],
    ["Marietta House", 1823]],
    columns=["building", "established"],
).set_index("building")

building_records_2020 = pd.DataFrame(
    [["Sam’s Bakery", 1962],
    ["Grande Hotel", 1830],
    ["Public Library", 1835],
    ["Mayberry’s Factory", 1924]],
    columns=["building", "established"],
).set_index("building")

print(building_records_1844)

print(building_records_2020)

print(building_records_1844.join(building_records_2020, how="inner", rsuffix="_2000"))
