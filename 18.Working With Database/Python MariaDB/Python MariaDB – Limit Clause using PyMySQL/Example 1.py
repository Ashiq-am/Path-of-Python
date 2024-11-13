import pymysql

# Create a connection object
# IP address of the MySQL database server
Host = "localhost"

# User name of the database server
User = "user"

# Password for the database user
Password = ""

database = "GFG"

conn = pymysql.connect(host=Host, user=User, password=Password, database)

# Create a cursor object
cur = conn.cursor()


query = f"SELECT price,PRODUCT_TYPE FROM PRODUCT WHERE price > 10000 LIMIT 2"

cur.execute(query)

rows = cur.fetchall()
for row in rows :
	print(row)

conn.close()
