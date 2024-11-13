import psycopg2
from psycopg2 import OperationalError

try:
    conn = psycopg2.connect(
        dbname="GeeksForGeeks",
        user="username",
        password="password",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
except OperationalError as e:
    print(f"Connection failed: {e}")
