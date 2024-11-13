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

# SQL INSERT statement
insert_query = """
INSERT INTO students (name, age, course)
VALUES (%s, %s, %s);
"""

# Data to be inserted (batch)
data = [
    ('Shalini', 21, 'Python'),
    ('Arun', 22 , 'Java'),
    ('Anvay', 22, 'C++')
]

# Executing the batch INSERT statement
cursor.executemany(insert_query, data)

# Committing the transaction
connection.commit()

# Print success message
print("Batch data inserted successfully!")

# Output
for record in data:
    print(f"Inserted data: {record}")

# Closing the cursor and connection
cursor.close()
connection.close()
