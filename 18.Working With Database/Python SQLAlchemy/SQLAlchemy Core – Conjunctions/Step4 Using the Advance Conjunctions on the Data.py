# Query the database using advanced conjunctions
query = students.select().where(
	and_(
		or_(
			students.c.age >= 30,
			students.c.name == 'Alice'
		),
		not_(students.c.gender == 'Male')
	)
)

result = conn.execute(query)

# Print the results
for row in result:
	print(row)
