import psycopg2

# establishing the connection
conn = psycopg2.connect(
	database="test",
	user='postgres',
	password='password',
	host='localhost',
	port='5432'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql = '''CREATE TABLE WORKER(
ID BIGSERIAL NOT NULL PRIMARY KEY,
NAME VARCHAR(100) NOT NULL,
COUNTRY VARCHAR(50) NOT NULL,
AGE INT,
SALARY FLOAT	
)'''
cursor.execute(sql)

# Inserting values into the table
insert_stmt = "INSERT INTO WORKER (NAME, COUNTRY, AGE, SALARY) \
VALUES (%s, %s, %s, %s)"
data = [('Krishna', 'India', 19, 2000),
		('Harry', 'USA', 20, 7000),
		('Malang', 'Nepal', 25, 5000),
		('Apple', 'London', 26, 2000),
		('Vishnu', 'India', 29, 2000),
		('Frank', 'UAE', 21, 7000),
		('Master', 'USA', 25, 5000),
		('Montu', 'India', 26, 2000),
		]
cursor.executemany(insert_stmt, data)

# Retrieving specific records using the where clause
cursor.execute("SELECT * from WORKER WHERE AGE <23")
print(cursor.fetchall())

# Retrieving specific records using the where clause
cursor.execute("SELECT * from WORKER WHERE COUNTRY='India' ")
print(cursor.fetchall())


# Retrieving name of employees whose salary is 5000
cursor.execute("SELECT name from WORKER WHERE salary=5000 ")
print(cursor.fetchall())

# Retrieving name and contry of employees whose salary is 2000
cursor.execute("SELECT name, country from WORKER WHERE salary=2000 ")
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
