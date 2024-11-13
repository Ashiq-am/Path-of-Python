from turtle import st
from mysqlx import Row
import psycopg2

DB_NAME = "tkgafrwp"
DB_USER = "tkgafrwp"
DB_PASS = "iYYtLAXVbid-i6MV3NO1EnU-_9SW2uEi"
DB_HOST = "tyke.db.elephantsql.com"
DB_PORT = "5432"
conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,
						host=DB_HOST,port=DB_PORT)
print("Database connected successfully")

cur = conn.cursor()
cur.execute("DELETE FROM Employee WHERE ID =1 ")
conn.commit()
print("Data deleted Successfully")
print("Total row affected "+str(cur.rowcount))
conn.close()
