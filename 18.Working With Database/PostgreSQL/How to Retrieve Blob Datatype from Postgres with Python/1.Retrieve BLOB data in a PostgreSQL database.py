import psycopg2
from config import config

# connect to the PostgreSQL server
# & creating a cursor object
conn = psycopg2.connect(**config)
cur = conn.cursor()

# Retrieve BLOB data from the database.
cur.execute('SELECT * FROM BLOB_DataStore')
db = cur.fetchall()

BLOB = db[0][2]
open("FromDB"+db[0][1], 'wb').write(BLOB)

cur.close()
conn.commit()
