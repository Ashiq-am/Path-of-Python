import psycopg2

# Correct Information
datetime_value = '2024-07-22 14:30:00'

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
