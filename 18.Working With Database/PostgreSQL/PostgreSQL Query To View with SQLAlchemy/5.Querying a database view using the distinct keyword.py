query = select().select_from(
demo_view).with_only_columns(
	demo_view.c.name).distinct()

# execute the query and print the results
with engine.connect() as conn:
	result = conn.execute(query).fetchall()
	for row in result:
		print(row)
