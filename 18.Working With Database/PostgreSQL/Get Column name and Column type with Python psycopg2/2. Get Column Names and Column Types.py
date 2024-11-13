import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Query to get column names and types
table_name = 'employee'
cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")

# Fetch all results
columns = cur.fetchall()

# Display column names and types
print("Column Name\t\tColumn Type")
print("-" * 40)
for column in columns:
    print(f"{column[0]}\t\t{column[1]}")

# Close the cursor and connection
cur.close()
conn.close()
