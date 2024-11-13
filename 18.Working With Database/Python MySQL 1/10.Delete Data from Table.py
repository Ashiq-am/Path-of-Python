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

query = "DELETE FROM STUDENT WHERE NAME = 'Ram'"
cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()
