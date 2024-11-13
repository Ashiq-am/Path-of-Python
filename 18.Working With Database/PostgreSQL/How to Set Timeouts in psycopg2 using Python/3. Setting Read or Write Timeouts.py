import psycopg2
from psycopg2 import OperationalError

# Custom function to set timeout
def set_socket_timeout(conn, timeout):
    with conn.cursor() as cursor:
        cursor.execute(f"SET statement_timeout = {timeout}")

try:
    conn = psycopg2.connect(
        dbname="postgres1",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    set_socket_timeout(conn, '5000')  # timeout in milliseconds
    cursor = conn.cursor()
    cursor.execute("SELECT pg_sleep(10)")  # This query will run for 10 seconds
    print("Query executed successfully")
except OperationalError as e:
    print(f"Read/Write operation failed: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
