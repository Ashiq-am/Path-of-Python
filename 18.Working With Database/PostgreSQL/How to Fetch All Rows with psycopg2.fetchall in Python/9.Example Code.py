import psycopg2

#Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="GeeksForGeeks",
    user="username",
    password="password",
    host="localhost",
    port="5432"
)

#Create a cursor object
cur = conn.cursor()

#Execute a SELECT query
cur.execute("SELECT * FROM GeeksTable")

#Fetch all rows from the result set
rows = cur.fetchall()

#Process the fetched data (e.g., print each row)
for row in rows:
    print(row)

# Step 6: Close the cursor and connection
cur.close()
conn.close()
