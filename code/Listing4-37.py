import pandas as pd


SQL = session.query(User).selectable

results = engine.execute(sql).fetchall()

data = {
    columns[col]: np.array([row[col] for row in results], dtype=type(results[0][col]))
    for col, v in enumerate(results[0])
}

df = pd.DataFrame(data)

print(df.dtypes)
