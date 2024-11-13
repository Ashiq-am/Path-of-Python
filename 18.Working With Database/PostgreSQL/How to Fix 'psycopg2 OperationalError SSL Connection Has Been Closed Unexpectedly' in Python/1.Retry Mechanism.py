import psycopg2
import time

def connect_to_db():
    retry_attempts = 5
    for attempt in range(retry_attempts):
        try:
            connection = psycopg2.connect(
                dbname="testdb",
                user="user",
                password="password",
                host="localhost",
                port="5432",
                sslmode="require"
            )
            return connection
        except psycopg2.OperationalError as e:
            print(f"Connection failed: {e}")
            time.sleep(5)
    return None

connection = connect_to_db()
if connection:
    print("Connected to the database")
