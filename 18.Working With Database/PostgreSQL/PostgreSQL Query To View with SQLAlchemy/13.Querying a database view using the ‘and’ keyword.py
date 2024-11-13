query = select().select_from(
demo_view).where(
and_(demo_view.c.name == "John", demo_view.c.id == 1))

# execute the query and print the results
with engine.connect() as conn:
	result = conn.execute(query).fetchall()
	for row in result:
		print(row)
