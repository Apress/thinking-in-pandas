import pandas as pd


gene_group1 = pd.DataFrame(
    [["Myc", 2, 0.05],
    ["BRCA1", 3, 0.01],
    ["BRCA2", 8, 0.02]],
    columns=["id", "FC1", "P1"],
).set_index(["id"])

gene_group2 = pd.DataFrame(
    [["Myc", 2, 0.05],
    ["BRCA1", 3, 0.01],
    ["Notch1", 2, 0.03],
    ["BRCA2", 8, 0.02]],
    columns=["id", "FC2", "P2"],
).set_index(["id"])

print(gene_group1)

print(gene_group2)

print(pd.merge(gene_group1, gene_group2, how="outer", on=["id"]))
