# Create a dataframe
# object from dictionary
df1 = pd.DataFrame({'Names' : ['Sonia', 'Priya'],
					'DOB':['18/10/2009','14/06/2009']})

# appending new data frame
# to existing data frame
df1.to_sql('Employee_Data',
		con = engine,
		if_exists = 'append')

# run a sql query
print(engine.execute("SELECT * FROM Employee_Data").fetchall())
