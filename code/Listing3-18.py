import pandas as pd

restaurant_inspections = pd.DataFrame(
    {
        "restaurant": ["Diner", "Diner", "Pandas", "Pandas"],
        "location": [(4, 2), (4, 2), (5, 4), (5, 4)],
        "date": ["02/18", "05/18", "02/18", "05/18"],
        "score": [90, 100, 55, 60],
    }
)
print(restaurant_inspections)

total_inspections = restaurant_inspections.groupby(
    ["restaurant", "location"], as_index=False
)["score"].count()

total_inspections.rename(columns={"score": "total"}, inplace=True)
print(total_inspections)
restaurant_inspections = pd.merge(
    restaurant_inspections, total_inspections, how="outer"
)
print(restaurant_inspections)
