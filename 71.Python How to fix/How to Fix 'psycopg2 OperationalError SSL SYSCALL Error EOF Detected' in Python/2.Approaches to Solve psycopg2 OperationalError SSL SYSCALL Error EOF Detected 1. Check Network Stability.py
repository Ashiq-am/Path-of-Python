import psycopg2
from time import sleep

def connect_with_retries(retries=3):
    attempt = 0
    while attempt < retries:
        conn = psycopg2.connect(
            dbname="postgres1",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432",
            # sslmode="require"
        )
        return conn
        sleep(5)
        attempt += 1

conn = connect_with_retries()
cursor = conn.cursor()

# Create a sample table and insert some data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sample_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50)
    )
""")

cursor.execute("INSERT INTO sample_table (name) VALUES ('Alice'), ('Bob'), ('Charlie')")

cursor.execute("SELECT * FROM sample_table")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
