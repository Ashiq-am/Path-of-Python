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

cur = conn.cursor() # creating a cursor

# executing queries to create table
cur.execute("""
CREATE TABLE Employee
(
	ID INT PRIMARY KEY NOT NULL,
	NAME TEXT NOT NULL,
	EMAI TEXT NOT NULL
)
""")

# commit the changes
conn.commit()
print("Table Created successfully")
