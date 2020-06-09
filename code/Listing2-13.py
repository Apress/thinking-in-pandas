import pandas as pd


trial_a_records = pd.DataFrame(
    [[230858, "John"],
    [237340, "May"],
    [240932, "Catherine"],
    [124093, "Ahmed"]],
    columns=["patient", "name"],
).set_index("patient")

trial_b_records = pd.DataFrame(
    [[210858, "Abi"],
    [237340, "May"],
    [240932, "Catherine"],
    [154093, "Julia"]],
    columns=["patient", "name"],
).set_index("patient")

print(trial_a_records)

print(trial_b_records)


both_trials = pd.merge(trial_a_records, trial_b_records, how="outer", right_index=True, left_index=True, indicator=True, on="name")
print(both_trials)


print(both_trials.query('_merge != "both"').drop("_merge", 1))


both_trials = (
    pd.merge(trial_a_records, trial_b_records, how="outer", right_index=True, left_index=True, indicator=True, on="name")
    .query('_merge != "both"')
    .drop("_merge", 1)
)
