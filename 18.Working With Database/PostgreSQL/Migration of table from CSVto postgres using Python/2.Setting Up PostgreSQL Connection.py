import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="gfgdb",
    user="postgres",
    password="1234"
)
cursor = conn.cursor()
