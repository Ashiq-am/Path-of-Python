import psycopg2

conn = psycopg2.connect(
    dbname="postgr1", # corrected
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
