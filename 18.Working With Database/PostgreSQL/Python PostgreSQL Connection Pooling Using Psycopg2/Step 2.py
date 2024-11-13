connection1 = pool.getconn()

# Use the connection to execute a query
cursor = connection1.cursor()
print("Results from Connection1: \n")
cursor.execute('SELECT * FROM person ORDER BY id')
results = cursor.fetchall()
for data in results:
	print(data)
	print()
