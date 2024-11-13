# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="user",
passwd ="password",
database = "gfg"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "UPDATE STUDENT SET AGE = 23 WHERE Name ='Ram'"
cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()
