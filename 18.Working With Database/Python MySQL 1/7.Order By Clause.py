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

query = "SELECT * FROM STUDENT ORDER BY NAME DESC"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
