import pandas as pd

restaurant_inspections = pd.DataFrame(
    {
        "restaurant": ["Diner", "Diner", "Pandas", "Pandas"],
        "location": [(4, 2), (4, 2), (5, 4), (5, 4)],
        "date": ["02/18", "05/18", "04/18", "01/18"],
        "score": [90, 100, 55, 60],
    }
)

print(restaurant_inspections)
