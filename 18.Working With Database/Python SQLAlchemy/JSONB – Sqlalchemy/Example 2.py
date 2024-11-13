data = {
	'name': 'Vik',
	'age': 30,
	'job_title': 'Data Scientist'
}

insert_stmt = insert(users).values(data=data)
conn = engine.connect()
conn.execute(insert_stmt)
conn.commit()
