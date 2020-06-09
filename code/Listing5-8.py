import pandas as pd
import numpy as np


patient_list = pd.DataFrame(
    [["O+", 2394, "hbp"], ["B+", 2312, np.nan], ["O-", 23409, "lbp"]],
    columns=["blood_type", "id", "history"],
).set_index(["blood_type"])

drug_table = pd.DataFrame(
    [
        ["ADF", "ADF", "ACB", "DCB", "ACE", "BAB"],
        ["GCB", "RAB", "DF", "EFR", np.nan, "HEF"],
        ["RAB", np.nan, np.nan, np.nan, np.nan, np.nan],
    ],
    columns=["O+", "O-", "A+", "A-", "B+", "B-"],
)

print(patient_list)
print(drug_table)
drug_table = drug_table.transpose(copy=False)
print(drug_table)
print(patient_list.join(drug_table))
