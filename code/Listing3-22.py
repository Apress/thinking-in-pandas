import pandas as pd

restaurants = pd.MultiIndex.from_tuples(
    (("Diner", (4, 2)), ("Pandas", (5, 4))),
    names=["restaurant", "location"],
)

inspections = pd.MultiIndex.from_tuples(
    ((0, "score"), (0, "date"), (1, "score"), (1, "date")), names=["inspection", "data"]
)

restaurant_inspections = pd.DataFrame(
    [[90, "02/18", 100, "05/18"], [55, "04/18", 76, "01/18"]],
    index=restaurants,
    columns=inspections,
)
print(restaurant_inspections)


total = restaurant_inspections.iloc[
    :, restaurant_inspections.columns.get_level_values("data") == "score"
].count()

new_index = pd.DataFrame(
    total.values, columns=["total"], index=restaurant_inspections.index
)

new_index.set_index("total", append=True, inplace=True)

restaurant_inspections.index = new_index.index
print(restaurant_inspections)
