import psycopg2

# Establish a connection
conn = psycopg2.connect(
    dbname="yourdbname",
    user="yourusername",
    password="yourpassword",
    host="yourhost",
    port="yourport"
)

# Perform database operations
# ...

# Close the connection
conn.close()
