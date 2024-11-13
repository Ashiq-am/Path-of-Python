import psycopg2

# Define connection parameters
connection_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '12345678',
    'host': 'localhost',
    'port': '5432'
}

# Establishing the connection
connection = psycopg2.connect(**connection_params)

# Creating a cursor object
cursor = connection.cursor()

# Print the connection status
print("Connection established!")

# Close the cursor and connection
cursor.close()
connection.close()
