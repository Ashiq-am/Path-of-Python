import psycopg2.pool

# Create a connection pool with a minimum of 2 connections and
#a maximum of 3 connections
pool = psycopg2.pool.SimpleConnectionPool(
	2, 3, user='postgres', password='test123',
	host='localhost', port='5432', database='test')

# Get a connection from the pool
connection1 = pool.getconn()

# Use the connection to execute a query
cursor = connection1.cursor()
print("Results from Connection1: \n")
cursor.execute('SELECT * FROM person ORDER BY id')
results = cursor.fetchall()
for data in results:
	print(data)
	print()

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

# Since maximum number of connections in the pool #
#is 3 and three connections
#are already made and not released yet.
#So, requesting for a fourth connection gives error.

# connection4 = pool.getconn()
# cursor = connection4.cursor()
# print("Results from Connection3: \n")
# cursor.execute('SELECT * FROM person ORDER BY id')
# results = cursor.fetchall()
# for data in results:
#	 print(data)
#	 print()


# Release the connection back to the pool
pool.putconn(connection1)
pool.putconn(connection2)
pool.putconn(connection3)
