import psycopg2

# Establishing connection with database2
conn2 = psycopg2.connect(
	database="database2",
	user="username",
	password="password",
	host="localhost",
	port="5432"
)
print("Successful Connection!!")

# Querying data
cur2 = conn2.cursor()
cur2.execute("SELECT * FROM employees")
rows = cur2.fetchall()
for row in rows:
	print(row)

# Closing connection
cur2.close()
conn2.close()
print("Connection closed!!!")
