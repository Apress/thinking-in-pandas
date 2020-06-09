import pandas as pd


select_user0 = session.query(Patient).filter_by(id=0).selectable

print(pd.read_sql(sql=select_user0, con=engine, columns=["id", "name"]))
