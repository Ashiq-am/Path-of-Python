query = select('*').select_from(demo_view).where(
	not_(demo_view.c.name == "John")
)

# execute the query and print the results
with engine.connect() as conn:
	result = conn.execute(query).fetchall()
	for row in result:
		print(row)
