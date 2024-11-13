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

# drop table if it already exists
cursorObject.execute("DROP TABLE IF EXISTS PHONE_RECORD")

# creating table
phoneRecord = """CREATE TABLE PHONE_RECORD ( 
				NAME VARCHAR(20) NOT NULL, 
				PHONE VARCHAR(10) NOT NULL 
				)"""

# table created
cursorObject.execute(phoneRecord)

# inserting data into the table
query = "INSERT INTO PHONE_RECORD (NAME, PHONE) VALUES (% s, % s)"
attrValues = ("Rituraj Saha", "9163089075")
cursorObject.execute(query, attrValues)

# deleting query
query = "DELETE FROM STUDENT WHERE NAME = 'Rituraj Saha'"
cursorObject.execute(query)

dataBase.commit()

# disconnecting from server
dataBase.close()
