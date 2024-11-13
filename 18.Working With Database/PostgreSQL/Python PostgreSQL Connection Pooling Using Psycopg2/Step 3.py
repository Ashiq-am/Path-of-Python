connection2 = pool.getconn()

# Use the connection to execute a query
cursor = connection2.cursor()
print("Results from Connection2: \n")
cursor.execute('SELECT * FROM person ORDER BY id')
results = cursor.fetchall()
for data in results:
	print(data)
	print()

connection3 = pool.getconn()

# Use the connection to execute a query
cursor = connection3.cursor()
print("Results from Connection3: \n")
cursor.execute('SELECT * FROM person ORDER BY id')
results = cursor.fetchall()
for data in results:
	print(data)
	print()
