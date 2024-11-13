import psycopg2

# Incorrect data type
datetime_value = 1234567890  # Integer instead of datetime

connection = psycopg2.connect(database="postgres1", user="postgres", password="1234")
cursor = connection.cursor()

# Create table if it doesn't exist
cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
        id SERIAL PRIMARY KEY,
        event_time TIMESTAMP
    )
    """)

# Insert data into the table
cursor.execute("INSERT INTO events (event_time) VALUES (%s)", (datetime_value,))
connection.commit()

print("Data inserted successfully")

cursor.close()
connection.close()
