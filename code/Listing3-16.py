import pandas as pd

restaurants = pd.MultiIndex.from_tuples(
    (("Diner", (4, 2)), ("Diner", (4, 2)), ("Pandas", (5, 4)), ("Pandas", (5, 4))),
    names=["restaurant", "location"],
)

restaurant_inspections = pd.DataFrame(
    {"date": ["02/18", "05/18", "04/18", "01/18"], "score": [90, 100, 55, 76]},
    index=restaurants,
)

print(restaurant_inspections)
