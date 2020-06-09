import pandas as pd


print(pd.read_sql(sql=User.__tablename__, con=engine, columns=["id", "name"]))
