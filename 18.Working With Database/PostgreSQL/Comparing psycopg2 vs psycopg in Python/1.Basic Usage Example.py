import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    dbname="GeeksData",
    user="username",
    password="password",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM Geekstable")

# Fetch one result
result = cursor.fetchone()

print(result)

# Close the cursor and connection
cursor.close()
connection.close()
