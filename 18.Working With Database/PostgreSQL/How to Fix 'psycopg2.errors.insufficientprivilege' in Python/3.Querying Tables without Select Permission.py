import psycopg2

conn = psycopg2.connect(dbname="exampledb", user="user", password="password")
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM test_table;")
    records = cursor.fetchall()
    print(records)
except psycopg2.errors.InsufficientPrivilege as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
