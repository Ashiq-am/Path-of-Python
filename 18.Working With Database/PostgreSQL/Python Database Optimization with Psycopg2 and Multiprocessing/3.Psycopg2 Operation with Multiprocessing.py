import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data text);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
for i in range(128):
	cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (i, str(i)))

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
