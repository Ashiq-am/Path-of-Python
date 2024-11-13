import psycopg2

conn = psycopg2.connect(
    dbname="postgres1",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
    connect_timeout=10  # timeout in seconds
)

print('connected')
