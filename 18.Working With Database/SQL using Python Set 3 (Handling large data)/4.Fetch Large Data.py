import sqlite3

# Connection created with the
# database using sqlite3.connect()
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# Create Table command executed
sql = """ 
		CREATE TABLE employee ( 
		ID INTEGER PRIMARY KEY, 
		fname VARCHAR(20), 
		lname VARCHAR(30), 
		gender CHAR(1), 
		dob DATE);"""
cursor.execute(sql)

# Single Tuple inserted
sql = """ 
		INSERT INTO employee 
		VALUES (1007, "Will", "Olsen", "M", "24-SEP-1865");"""
cursor.execute(sql)

# Multiple Rows inserted
List = [(1008, 'Rkb', 'Boss', 'M', "27-NOV-1864"),
		(1098, 'Sak', 'Rose', 'F', "27-DEC-1864"),
		(1908, 'Royal', 'Bassen', "F", "17-NOV-1894")]

connection. executemany(
		"INSERT INTO employee VALUES (?, ?, ?, ?, ?)", List)

print("Method-1\n")

# Multiple Rows fetched from
# the Database
for row in connection.execute('SELECT * FROM employee ORDER BY ID'):
		print (row)

print("\nMethod-2\n")

# Method-2 to fetch multiple
# rows
sql = """ 
		SELECT * FROM employee ORDER BY ID;"""

cursor.execute(sql)
result = cursor.fetchall()

for x in result:
	print(x)

connection.commit()
connection.close()










"""Note: This piece of code may not work on online interpreters, due to permission privileges to create/write database."""
