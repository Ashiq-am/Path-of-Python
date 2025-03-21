# importing psycopg2 module
import psycopg2

# establishing the connection
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='password',
	host='localhost',
	port='5432'
)

# creating cursor object
cursor = conn.cursor()

# query to sort table by name
sql2 = 'select * from employee;'
# executing query
cursor.execute(sql2)

# fetching the result
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
