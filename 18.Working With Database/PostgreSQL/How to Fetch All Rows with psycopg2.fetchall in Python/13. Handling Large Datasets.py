import psycopg2

conn = psycopg2.connect(
    dbname="GeeksForGeeks",
    user="username",
    password="password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Use a named cursor for server-side cursor
cur.execute("DECLARE cursor CURSOR FOR SELECT * FROM GeeksTable")

while True:
    cur.execute("FETCH 1000 FROM cursor")
    rows = cur.fetchall()
    if not rows:
        break
    for row in rows:
        print(row)

cur.close()
conn.close()
