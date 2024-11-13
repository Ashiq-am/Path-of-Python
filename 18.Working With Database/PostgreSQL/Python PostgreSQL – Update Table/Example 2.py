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

# create a cursor object
cursor = conn.cursor()

# query to update table
sql='''update Geeks set state='Delhi' where id='2'; '''

# execute the qury
cursor.execute(sql)
print("Table updated..")

print('Table after updation...')

# query to display Geeks table
sql2='select * from Geeks;'

# execute query
cursor.execute(sql2);

# fetching all details
print(cursor.fetchall());

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
