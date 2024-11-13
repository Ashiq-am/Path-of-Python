import psycopg2
from psycopg2 import sql, OperationalError

try:
    conn = psycopg2.connect(
        dbname="postgres1",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SET statement_timeout = %s", ('5000',))  # timeout in milliseconds

    query = sql.SQL("SELECT pg_sleep(10)")  # This query will run for 10 seconds
    cursor.execute(query)
    print("Query executed successfully")
except OperationalError as e:
    print(f"Query failed: {e}")
finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
