import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="gfg"
)

mycursor = mydb.cursor()

mycursor.execute("Show tables;")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)
