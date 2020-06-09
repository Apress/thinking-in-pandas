import pandas as pd


temp_county_a = pd.DataFrame(
    [[(4,5), 35.6],
    [(1,2), 37.4],
    [(6,4), 36.3],
    [(1,7), 40.2]],
    columns=["location", "temp"],
).set_index(["location"])

temp_county_b = pd.DataFrame(
    [[(6,4), 34.2],
    [(0,4), 33.7],
    [(3,8), 38.1],
    [(1,5), 37.0]],
    columns=["location", "temp"],
).set_index(["location"])


print(temp_county_a)

print(temp_county_b)

print(pd.concat([temp_county_a, temp_county_b]))
