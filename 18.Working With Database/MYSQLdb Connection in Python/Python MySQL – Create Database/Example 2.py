''''''


"""Let’s suppose we want to create a table in the database, then we need to connect to a database. 
Below is a program to create a table in the geeks4geeks database which was created in the above program."""





# importing required library
import mysql.connector

# connecting to the database
dataBase = mysql.connector.connect(
					host = "localhost",
					user = "user",
					passwd = "gfg",
					database = "geeks4geeks" )

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE STUDENT ( 
				NAME VARCHAR(20) NOT NULL, 
				BRANCH VARCHAR(50), 
				ROLL INT NOT NULL, 
				SECTION VARCHAR(5), 
				AGE INT, 
				)"""

# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()
