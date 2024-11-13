# Establish connection to MySQL database
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root123",
database = "geeks"
)
mycursor = mydb.cursor()

query = " DELETE FROM EMPLOYEE WHERE INCOME = '5000';"
mycursor.execute(query)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
mydb.close()
