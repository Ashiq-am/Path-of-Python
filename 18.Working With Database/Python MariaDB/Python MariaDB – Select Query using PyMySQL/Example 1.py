import pymysql

# Create a connection object
# IP address of the MySQL database server
Host = "localhost"

# User name of the database server
User = "user"

# Password for the database user
Password = ""

database = "GFG"

conn = pymysql.connect(host=Host, user=User, password=Password, database=database)

# Create a cursor object
cur = conn.cursor()


query = f"SELECT * FROM PRODUCT"

cur.execute(query)

rows = cur.fetchall()
conn.close()

for row in rows :
	print(row)
