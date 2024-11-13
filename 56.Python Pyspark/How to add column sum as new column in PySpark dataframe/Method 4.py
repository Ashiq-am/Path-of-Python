# select everything from table df_col1 and
# create new sum column as " select_method_sum".
df_col1 = df_col1.select('*',
						(df_col1["B"]+df_col1["C"]+df_col1['D']).
						alias("select_method_sum"))

# Showing the schema and table
df_col1.printSchema()
df_col1.show()
