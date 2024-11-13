# import packages
import psycopg2
from datetime import datetime, timezone

# establish connection
conn = psycopg2.connect(
	database="Banking", user='postgres', password='pass',
	host='127.0.0.1', port='5432'
)

# autocommit is set to True
conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

# creating a table
cursor.execute(
	'create table bank_records(amount_deposited decimal , Date timestamptz);')

deposit_amount = 4565.89
dt = datetime.now(timezone.utc)

# inserting values
cursor.execute('insert into bank_records values(%s,%s)', (deposit_amount, dt,))

# fetching rows
sql1 = '''select * from bank_records;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

conn.commit()

# closing the connection
conn.close()
