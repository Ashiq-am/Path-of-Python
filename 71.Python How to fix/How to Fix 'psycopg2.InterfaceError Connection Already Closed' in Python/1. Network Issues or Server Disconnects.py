import psycopg2

conn = psycopg2.connect(dbname="postgres1", user="postgres", password="1234", host="localhost")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_name (
        id SERIAL PRIMARY KEY,
        column1 VARCHAR(255),
        column2 INT
    );
    """)

cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()
conn.close()  # Simulating network issue or server disconnect
cursor.execute("SELECT * FROM another_table")  # Raises InterfaceError

print(f"InterfaceError: {e}")

if conn:
    conn.close()
