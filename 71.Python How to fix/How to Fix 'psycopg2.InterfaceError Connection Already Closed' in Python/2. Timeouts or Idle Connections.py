import psycopg2
from psycopg2 import OperationalError


conn = psycopg2.connect(dbname="mydb", user="user", password="password", host="localhost")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_name (
        id SERIAL PRIMARY KEY,
        column1 VARCHAR(255),
        column2 INT
    );
    """)
cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()
    # Assume there's a timeout or the connection becomes idle
conn.rollback()  # Simulating a timeout or idle connection
cursor.execute("SELECT * FROM another_table")  # Raises InterfaceError
