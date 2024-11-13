import psycopg2

# connection establishment
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='password',
	host='localhost',
	port='5432'
)

conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

# query to create a table
sql = ''' CREATE TABLE demo
(
	id INT,
	name VARCHAR(50),
	city VARCHAR(50),
	age INT
); '''

# executing above query
cursor.execute(sql)
print("Table has been created successfully!!")

# Closing the connection
conn.close()
