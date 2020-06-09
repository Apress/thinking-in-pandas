import pandas as pd

arrivals_by_destination = (
    pd.DataFrame(
        [
            [2015, "BER", 20, 0],
            [2015, "LON", 10, 5],
            [2016, "BER", 15, 10],
            [2016, "LON", 10, 0],
        ],
        columns=["date", "place", "0", "1"],
    )
    .set_index(["date", "place"])
    .sort_index()
)

print(arrivals_by_destination)

arrivals_by_destination["total"] = arrivals_by_destination.sum()
