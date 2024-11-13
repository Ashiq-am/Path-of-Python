import psycopg2
from psycopg2 import OperationalError, InterfaceError

def execute_query(query):
    conn = None
    try:
        conn = psycopg2.connect(dbname="postgres1", user="postgres", password="1234", host="localhost")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS table_name (
                id SERIAL PRIMARY KEY,
                column1 VARCHAR(255),
                column2 INT
            );
        """)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except (OperationalError, InterfaceError) as e:
        print(f"Database error: {e}")
        # Attempt to reconnect if the connection was lost
        try:
            conn = psycopg2.connect(dbname="mydb", user="user", password="password", host="localhost")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS table_name (
                    id SERIAL PRIMARY KEY,
                    column1 VARCHAR(255),
                    column2 INT
                );
            """)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Reconnection failed: {e}")
    finally:
        if conn:
            conn.close()

# Usage
result = execute_query("SELECT * FROM table_name")
print(result)
