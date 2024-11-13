query = select().select_from(
demo_view).order_by(
demo_view.c.created_at)

# execute the query and print the results
with engine.connect() as conn:
	result = conn.execute(query).fetchall()
	for row in result:
		print(row)
