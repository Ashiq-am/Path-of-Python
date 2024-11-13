# Query the database using conjunctions
query = students.select().where(
	or_(students.c.name == 'John', students.c.name == 'Jane'))

result = conn.execute(query)

# Print the results
for row in result:
	print(row)
