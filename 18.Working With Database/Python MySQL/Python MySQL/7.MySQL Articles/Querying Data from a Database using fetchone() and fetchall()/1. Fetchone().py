# Program to display the data
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "yourusername",
password = "yourpass",
database = "yourdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM CUSTOMERS")

result = mycursor.fetchone()

print(result)
