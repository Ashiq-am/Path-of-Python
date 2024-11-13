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
sql = '''CREATE TABLE Geeky(
id SERIAL NOT NULL,
name varchar(20) not null,
state varchar(20) not null
)'''
cursor.execute(sql)

# inserting values in it
cursor.execute('''INSERT INTO Geeky(name , state)\
	VALUES ('Babita','Bihar')''')
cursor.execute(
	'''INSERT INTO Geeky(name , state)\
	VALUES ('Anushka','Hyderabad')''')
cursor.execute(
	'''INSERT INTO Geeky(name , state)\
	VALUES ('Anamika','Banglore')''')
cursor.execute('''INSERT INTO Geeky(name , state)\
	VALUES ('Sanaya','Pune')''')
cursor.execute(
	'''INSERT INTO Geeky(name , state)\
	VALUES ('Radha','Chandigarh')''')

# query to update the existing record
# update state as Haryana where name is Radha
sql1 = "UPDATE Geeky SET state = 'Haryana' WHERE name = 'Radha'"
cursor.execute(sql1)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
