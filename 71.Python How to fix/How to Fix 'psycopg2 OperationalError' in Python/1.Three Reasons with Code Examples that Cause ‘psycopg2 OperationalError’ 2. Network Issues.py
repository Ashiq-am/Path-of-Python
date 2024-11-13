import psycopg2

conn = psycopg2.connect(
    dbname="postgres1",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
