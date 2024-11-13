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
            sslmode="require"
        )
        return conn
        sleep(5)
        attempt += 1

conn = connect_with_retries()
cursor = conn.cursor()
cursor.execute("SELECT * FROM yourtable")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
