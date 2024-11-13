query = select('*').select_from(
demo_view).where(
cast(
	demo_view.c.name, String
).in_(['John', 'Jane']))

# execute the query and print the results
with engine.connect() as conn:
	result = conn.execute(query).fetchall()
	for row in result:
		print(row)
