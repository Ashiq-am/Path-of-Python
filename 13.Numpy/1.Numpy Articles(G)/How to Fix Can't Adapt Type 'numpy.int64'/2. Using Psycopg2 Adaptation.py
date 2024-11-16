import numpy as np
import psycopg2
from psycopg2.extensions import register_adapter, AsIs

# Function to adapt numpy.int64 to PostgreSQL int
def adapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)

# Register the adapter
register_adapter(np.int64, adapt_numpy_int64)

# Example NumPy array
data = np.array([1, 2, 3, 4], dtype=np.int64)

# Inserting into PostgreSQL
conn = psycopg2.connect(database="your_db", user="your_user", password="your_password")
cur = conn.cursor()

for value in data:
    cur.execute("INSERT INTO your_table (column_name) VALUES (%s)", (value,))

conn.commit()
cur.close()
conn.close()
