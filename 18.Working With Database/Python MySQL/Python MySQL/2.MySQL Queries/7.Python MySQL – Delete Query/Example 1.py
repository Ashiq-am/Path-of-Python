# importing required library
import mysql.connector

# connecting to the database
dataBase = mysql.connector.connect(
					host = "localhost",
					user = "user",
					passwd = "pswrd",
					database = "geeks" )

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE STUDENT ( 
				NAME VARCHAR(20) NOT NULL, 
				BRANCH VARCHAR(50), 
				ROLL INT NOT NULL, 
				SECTION VARCHAR(5), 
				AGE INT 
				)"""

# table created
cursorObject.execute(studentRecord)

# inserting data into the table
query = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (% s, % s)"

attrValues = ("Rituraj Saha", "Information Technology", "1706256", "IT-3", "20")
cursorObject.execute(query, attrValues)

attrValues = ("Ritam Barik", "Information Technology", "1706254", "IT-3", "21")
cursorObject.execute(query, attrValues)

attrValues = ("Rishi Kumar", "Information Technology", "1706253", "IT-3", "21")
cursorObject.execute(query, attrValues)

# deleting query
query = "DELETE FROM STUDENT WHERE ROLL = 1706256"
cursorObject.execute(query, attrValues)

dataBase.commit()

# disconnecting from server
dataBase.close()
