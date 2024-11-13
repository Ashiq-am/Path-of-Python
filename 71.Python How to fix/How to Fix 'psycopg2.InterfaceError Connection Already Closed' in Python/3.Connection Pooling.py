import psycopg2
from psycopg2 import pool

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1, 10, dbname="mydb", user="user", password="password", host="localhost"
)


def execute_query(query):
    # Get a connection from the pool
    conn = connection_pool.getconn()
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

    # Return the connection back to the pool
    connection_pool.putconn(conn)
    return rows


# Usage
result = execute_query("SELECT * FROM table_name")
print(result)
