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

# creating table
sql = '''CREATE TABLE Geeks(
id SERIAL NOT NULL,
name varchar(20) not null,
state varchar(20) not null
)'''
cursor.execute(sql)

# inserting values in the table
cursor.execute('''INSERT INTO Geeks(name , state) VALUES ('Babita','Bihar')''')
cursor.execute(
	'''INSERT INTO Geeks(name , state) VALUES ('Anushka','Hyderabad')''')
cursor.execute(
	'''INSERT INTO Geeks(name , state) VALUES ('Anamika','Banglore')''')
cursor.execute('''INSERT INTO Geeks(name , state) VALUES ('Sanaya','Pune')''')
cursor.execute(
	'''INSERT INTO Geeks(name , state) VALUES ('Radha','Chandigarh')''')


# query to sort table by name
sql2 = 'select * from Geeks order by name;'
# executing query
cursor.execute(sql2)
# fetching records
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
