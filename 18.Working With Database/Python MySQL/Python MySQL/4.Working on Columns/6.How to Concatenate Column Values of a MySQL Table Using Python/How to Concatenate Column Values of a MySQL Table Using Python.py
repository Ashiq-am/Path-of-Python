# Establish connection to MySQL database
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root123",
database = "geeks"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT Concat(FirstName, LastName) AS fulldetail FROM Persons;")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
