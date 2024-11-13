# Update the title of the employee
update_query = text("""
	UPDATE employeest
	SET info = jsonb_set(info,
	'{job, title}', '"Data Scientist"', false)
	WHERE id = 10;
""")
# Print the query for verification
print(update_query)
# Execute the update query command
result = conn.execute(update_query)
print('update query results:', result.rowcount)
# Commit will allow to save the changes in the database
conn.commit()
