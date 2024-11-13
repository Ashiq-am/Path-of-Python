import psycopg2
from psycopg2 import ProgrammingError

conn = psycopg2.connect(
    dbname="GeeksForGeeks",
    user="username",
    password="password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

try:
    cur.execute("SELECT * FROM GeeksTable")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except ProgrammingError as e:
    print(f"Query failed: {e}")
finally:
    cur.close()
    conn.close()
