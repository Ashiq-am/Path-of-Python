# importing psycopg2 module
import psycopg2

# establishing the connection
conn = psycopg2.connect(
database="postgres",
	user='postgres',
	password='password',
	host='localhost',
	port= '5432'
)

# creating a curssor object
cursor = conn.cursor()

# query to update table with where clause
sql='''update Geeks set state='Kashmir'; '''

# execute the query
cursor.execute(sql)
print('table updated..')

print('table after updation...')
sql2='''select * from Geeks;'''
cursor.execute(sql2);

# print table after modification
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()# code
