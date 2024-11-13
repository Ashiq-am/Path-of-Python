# Establish connection to MySQL database
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root123",
database = "geeks"
)

#getting the cursor by cursor() method
mycursor = db.cursor()

insertQuery = " Select Value, IF(Value>1000,'MORE','LESS') from salary;"
mycursor.execute(insertQuery)
myresult = mycursor.fetchall()
print(myresult)

# close the Connection
db.close()
