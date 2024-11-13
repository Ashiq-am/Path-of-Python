# Import our psycopg2 module
import psycopg2

# Create a connection to our existing database
conn = psycopg2.connect(
user='user', password='pass'
)

# Open a cursor to perform operations
cur = conn.cursor()

# Assemble a SQL query
query = 'DROP database "TestDB";'

# Execute our query
cur.execute(query)

# Close our connection and cursor
cur.close()
conn.close()
