# insert some data into the demo view
with engine.connect() as conn:
	conn.execute(demo_view.insert(), [
		{'name': 'John', 'created_at': '2021-07-01'},
		{'name': 'Jane', 'created_at': '2021-07-02'},
		{'name': 'Joe', 'created_at': '2021-07-03'}
	])

	# commit the changes
	conn.commit()


# query the demo view to get name and created_at columns
query = select().select_from(demo_view).with_only_columns(
		demo_view.c.name, demo_view.c.created_at)
# execute the query and print the results
with engine.connect() as conn:
	result = conn.execute(query).fetchall()
	for row in result:
		print(row)
