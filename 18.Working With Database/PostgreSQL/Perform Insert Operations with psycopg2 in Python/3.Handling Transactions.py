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

try:
    # SQL INSERT statement
    insert_query = """
    INSERT INTO students (name, age, course)
    VALUES (%s, %s, %s);
    """

    # Data to be inserted
    data = [
        ('Shalini', 21, 'Python'),
        ('Arun', 22, 'Java')
    ]

    # Executing insert statements
    for record in data:
        cursor.execute(insert_query, record)

    # Committing the transaction
    connection.commit()
    print("Transaction committed successfully!")

except Exception as e:
    # Rolling back the transaction in case of error
    connection.rollback()
    print(f"Transaction rolled back due to error: {e}")

finally:
    # Closing the cursor and connection
    cursor.close()
    connection.close()
