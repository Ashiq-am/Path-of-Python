# Print the data we inserted, along with previous rows
select_query = employeest.select()
conn = engine.connect()
print('Connection status:', conn.closed)
result = conn.execute(select_query)
print('Select query results:', result.fetchall())

for row in result:
	print(row)
