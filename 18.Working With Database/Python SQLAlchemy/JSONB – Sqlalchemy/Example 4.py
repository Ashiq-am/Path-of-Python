# Update data

update_stmt = users.update().where(users.c.id == 1).values(
	data={'job_title': 'Software Engineer'})
conn.execute(update_stmt)
conn.commit()
