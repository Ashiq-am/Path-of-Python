# reading the sql database
# with index "Names"
df2 = pd.read_sql('Employee_Data',
				con = engine,
				index_col = 'Names',
				parse_dates = ['DOB'])
# show the dataframe
print(df2)

# print new line
print()

# show the type of df2
print(type(df2))
