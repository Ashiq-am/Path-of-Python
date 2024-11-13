# import the sqlite3 module
import sqlite3

# Define connection and cursor
connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES (1,'Rohit', 'Pathak', 21, 'IT')")
cursor.execute("INSERT INTO STUDENT VALUES (2,'Nitin', 'Biradar', 21, 'IT')")
cursor.execute("INSERT INTO STUDENT VALUES (3,'Virat', 'Kohli', 30, 'CIVIL')")
cursor.execute("INSERT INTO STUDENT VALUES (4,'Rohit', 'Sharma', 32, 'COMP')")

# printing the cursor data
if cursor:
	print("Data Inserted !")
else:
	print("Data Insertion Failed !")

# Commit the changes in database and Close the connection
connection.commit()
connection.close()
