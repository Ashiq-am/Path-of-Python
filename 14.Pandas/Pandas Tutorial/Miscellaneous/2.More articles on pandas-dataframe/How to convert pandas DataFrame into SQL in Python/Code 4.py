# acccesing only a particular
# column from the database
df3 = pd.read_sql('Employee_Data',
				con = engine,
				columns = ["Names"])
# show the data
print(df3)
