update_query = text("""
	UPDATE employees
	SET info = jsonb_set(info, '{projects, 1, name}', '"New Project Name"')
	WHERE id = :id
""")
conn = engine.connect()
conn.execute(update_query, id=1)
conn.close()
