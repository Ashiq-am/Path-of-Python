import psycopg2
import logging

# Setup logging
logging.basicConfig(filename='db_errors.log', level=logging.ERROR)

# Connection parameters
connection_params = {
    'dbname': 'Geeks',
    'user': 'username',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

try:
    # Establishing the connection
    connection = psycopg2.connect(**connection_params)
    cursor = connection.cursor()

    # SQL INSERT statement
    insert_query = """
    INSERT INTO geeksforgeeks (name, course, age)
    VALUES (%s, %s, %s);
    """

    # Data to be inserted
    data = [
        ('Shalini', 'Python', 'not_a_number')  # Deliberate error
    ]

    # Executing the INSERT statement
    cursor.executemany(insert_query, data)

    # Committing the transaction
    connection.commit()

except psycopg2.Error as e:
    # Log error message
    logging.error(f"Database error: {e.pgcode} - {e.pgerror}")
    print(f"An error occurred: {e.pgcode} - {e.pgerror}")

finally:
    # Closing the cursor and connection
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
