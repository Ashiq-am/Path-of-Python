# Define a query to count the number of rows in the "student" table
# for each unique value of the "dept" column
query = select(
	label('name_uppercase', func.count(table.c.dept)),
	table.c.dept
).group_by(table.c.dept)

# Execute the query and print the results
print('\nDisplaying records labels count department wise: \n')
with engine.connect() as conn:
	result = connection.execute(query)

	for row in result:
		print(row)
