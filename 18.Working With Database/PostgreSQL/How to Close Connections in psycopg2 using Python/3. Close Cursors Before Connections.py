import psycopg2

conn = psycopg2.connect(
    dbname="yourdbname",
    user="yourusername",
    password="yourpassword",
    host="yourhost",
    port="yourport"
)

try:
    # Create a cursor
    cur = conn.cursor()

    # Perform operations using the cursor
    # ...

    # Close the cursor
    cur.close()
finally:
    # Close the connection
    conn.close()
