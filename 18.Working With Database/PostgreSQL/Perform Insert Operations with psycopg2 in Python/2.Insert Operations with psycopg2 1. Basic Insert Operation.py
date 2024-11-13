import psycopg2

# Connection parameters
connection_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '12345678',
    'host': 'localhost',
    'port': '5432'
}

# Establishing the connection
connection = psycopg2.connect(**connection_params)
cursor = connection.cursor()

# Create table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    course VARCHAR(100)
);
"""
cursor.execute(create_table_query)

# SQL INSERT statement
insert_query = """
INSERT INTO students (name, age, course)
VALUES (%s, %s, %s);
"""

# Data to be inserted
data = ('Shalini', 21 , 'Python')

# Executing the INSERT statement
cursor.execute(insert_query, data)

# Committing the transaction
connection.commit()

# Print success message
print("Data inserted successfully!")

# Output
print(f"Inserted data: {data}")

# Closing the cursor and connection
cursor.close()
connection.close()
