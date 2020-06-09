result = self.pd_sql.execute(sql_select)

column_names = result.keys()

data = result.fetchall()

self.frame = DataFrame.from_records(
    data, columns=column_names, coerce_float=coerce_float
)
