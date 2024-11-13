import psycopg2
import csv

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

# Open the CSV file
with open('students.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    next(csv_reader)

    # Prepare data for insertion
    data = [row for row in csv_reader]

# Executing the batch INSERT statement
cursor.executemany(insert_query, data)

# Committing the transaction
connection.commit()

print("CSV data inserted successfully!")

# Closing the cursor and connection
cursor.close()
connection.close()
