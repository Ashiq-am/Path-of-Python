import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    dbname="yourdbname",
    user="yourusername",
    password="yourpassword",
    host="yourhost",
    port="yourport"
)

# Enable autocommit mode
conn.autocommit = True

# Now, any operations performed using this connection will be automatically committed
cur = conn.cursor()
cur.execute("YOUR SQL QUERY HERE")

# Clean up
cur.close()
conn.close()
