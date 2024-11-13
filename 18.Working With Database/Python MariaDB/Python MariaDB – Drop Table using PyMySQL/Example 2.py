import pymysql

# Create a connection object

conn = pymysql.connect('localhost', 'user', 'password', 'database')

# Create a cursor object
cur = conn.cursor()


query = f"DROP TABLE IF exists Student"

cur.execute(query)

rows = cur.fetchall()
conn.close()

for row in rows :
	print(row)
