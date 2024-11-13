import pymysql

# Create a connection object

conn = pymysql.connect('localhost', 'user',
						'password', 'database')

# Create a cursor object
cur = conn.cursor()

query = f"SELECT * FROM PRODUCT ORDER BY price DESC"

cur.execute(query)
for row in rows :
	print(row)

conn.close()
