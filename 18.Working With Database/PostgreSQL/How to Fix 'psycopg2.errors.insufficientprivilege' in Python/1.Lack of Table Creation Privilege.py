import psycopg2

try:
    conn = psycopg2.connect(dbname="exampledb", user="user", password="password")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));")
    conn.commit()
except psycopg2.errors.InsufficientPrivilege as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
