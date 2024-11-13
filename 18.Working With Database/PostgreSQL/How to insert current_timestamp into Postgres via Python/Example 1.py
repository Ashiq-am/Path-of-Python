# import packages
import psycopg2
from datetime import datetime, timezone

# establish a connection
conn = psycopg2.connect(
	database="TIMESTAMP_DATA", user='postgres', password='pass',
	host='127.0.0.1', port='5432'
)


conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

# creating a table
cursor.execute('''CREATE TABLE timestamp_data
(timestamp TIMESTAMP,timestamp_timezone TIMESTAMPTZ);''')

# inserting timestamp values
cursor.execute('''INSERT INTO timestamp_data VALUES
('2021-05-20 12:07:18-09','2021-05-20 12:07:18-09');''')

# fetching data
sql1 = '''select * from timestamp_data;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

conn.commit()

# closing the connection
conn.close()
