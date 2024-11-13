import pymysql

# Create a connection object
conn = pymysql.connect('localhost', 'user', 'password', 'database')

# Create a cursor object
cur = conn.cursor()


query = f"SELECT * FROM PRODUCT LIMIT 2 OFFSET 1"

cur.execute(query)

rows = cur.fetchall()
for row in rows :
	print(row)

conn.close()
