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

# Create a table
create_table_query = """
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    hire_date DATE
)
"""
cur.execute(create_table_query)
conn.commit()

print("Table created successfully")

# Close the cursor and connection
cur.close()
conn.close()
