# run a sql query in the database
# and store result in a dataframe
df5 = pd.read_sql_query('Select DOB from Employee_Data',
						con = engine,
						parse_dates = ['DOB'])
# show the dataframe
print(df5)
