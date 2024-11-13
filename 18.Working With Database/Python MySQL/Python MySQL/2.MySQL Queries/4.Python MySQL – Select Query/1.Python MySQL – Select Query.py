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

# disconnecting from server
dataBase.close()
