from mysqlx import Row
import psycopg2

DB_NAME = "tkgafrwp"
DB_USER = "tkgafrwp"
DB_PASS = "iYYtLAXVbid-i6MV3NO1EnU-_9SW2uEi"
DB_HOST = "tyke.db.elephantsql.com"
DB_PORT = "5432"
conn = psycopg2.connect(database=DB_NAME,
						user=DB_USER,
						password=DB_PASS,
						host=DB_HOST,
						port=DB_PORT)
print("Database connected successfully")

cur = conn.cursor()
cur.execute("SELECT * FROM Employee")
rows = cur.fetchall()
for data in rows:
	print("ID :" + str(data[0]))
	print("NAME :" + data[1])
	print("EMAIL :" + data[2])

print('Data fetched successfully')
conn.close()
