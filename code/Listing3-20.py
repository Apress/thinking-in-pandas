import pandas as pd

restaurants = pd.MultiIndex.from_tuples(
    (("Diner", (4, 2)), ("Pandas", (5, 4))),
    names=["restaurant", "location"],
)

restaurant_inspections = pd.DataFrame(
    {"02/18": [90, 55], "05/18": [100, 76]}, index=restaurants
)
print(restaurant_inspections)

restaurant_inspections["total"] = restaurant_inspections.count(axis=1)

restaurant_inspections.set_index(["total"], append=True, inplace=True)
print(restaurant_inspections)
