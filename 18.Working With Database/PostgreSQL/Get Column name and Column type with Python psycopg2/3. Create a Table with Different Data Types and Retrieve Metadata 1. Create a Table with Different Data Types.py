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

# Create a table with various data types
create_table_query = """
CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    price DECIMAL(10, 2),
    stock_quantity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
cur.execute(create_table_query)
conn.commit()

print("Table created successfully")

# Close the cursor and connection
cur.close()
conn.close()
