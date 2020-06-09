import pandas as pd


temp_device_a = pd.DataFrame(
    [[(4,5), 35.6],
    [(1,2), 37.4],
    [(6,4), 36.3],
    [(1,7), 40.2]],
    columns=["location", "temp"],
).set_index(["location"])

temp_device_b = pd.DataFrame(
    [[(4,5), 34.2],
    [(1,2), 36.7],
    [(6,4), 37.1],
    [(1,7), 39.0]],
    columns=["location", "temp"],
).set_index(["location"])


print(temp_device_a)

print(temp_device_b)

print(pd.concat([temp_device_a, temp_device_b], keys=["device_a", "device_b"], axis=1))
