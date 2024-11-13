import psycopg2

conn = psycopg2.connect(dbname="exampledb", user="user", password="password")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE test_table ADD COLUMN age INT;")
    conn.commit()
except psycopg2.errors.InsufficientPrivilege as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
