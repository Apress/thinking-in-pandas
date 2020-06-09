import pandas as pd


arrivals_by_destination = (
    pd.DataFrame(
        [
            [2015, "LON", 10],
            [2015, "BER", 20],
            [2015, "LON", 5],
            [2016, "LON", 10],
            [2016, "BER", 15],
            [2016, "BER", 10],
        ],
        columns=["date", "place", "number"],
    )
    .set_index(["date", "place"])
    .sort_index()
)

print(arrivals_by_destination)

groups = arrivals_by_destination.groupby(["date", "place"])

for idx, grp in groups:

    arrivals_by_destination.loc[idx, "total"] = grp["number"].sum()

print(arrivals_by_destination)
