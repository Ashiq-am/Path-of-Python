query = select().select_from(
demo_view).with_only_columns(
func.min(demo_view.c.id))

# execute the query and print the results
with engine.connect() as conn:
	result = conn.execute(query).fetchall()
	for row in result:
		print(row)
