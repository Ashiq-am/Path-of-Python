import numpy as np
import psycopg2

# Example NumPy array
data = np.array([1, 2, 3, 4], dtype=np.int64)

# Convert using list comprehension
data = [int(value) for value in data]

# Inserting into PostgreSQL
conn = psycopg2.connect(database="your_db", user="your_user", password="your_password")
cur = conn.cursor()

for value in data:
    cur.execute("INSERT INTO your_table (column_name) VALUES (%s)", (value,))

conn.commit()
cur.close()
conn.close()
