# get a particular column
# from a database in the
# form of list
df4 = pd.read_sql('Employee_Data',
				con = engine,
				index_col = 'Names',
				columns = ["Names"])
# show the data
print(df4)
