import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(user="yourusername", password="yourpassword",
                        host="localhost", database="yourdatabase")

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")

# Fetch results
results = cursor.fetchall()

# Close the connection
cursor.close()
conn.close()
