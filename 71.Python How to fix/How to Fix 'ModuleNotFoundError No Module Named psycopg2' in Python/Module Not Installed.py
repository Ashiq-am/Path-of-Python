import psycopg2
conn = psycopg2.connect(
    dbname="geeksforgeeks_db",
    user="gfguser",
    password="pass123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("SELECT * FROM articles WHERE source = 'GeeksforGeeks';")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
