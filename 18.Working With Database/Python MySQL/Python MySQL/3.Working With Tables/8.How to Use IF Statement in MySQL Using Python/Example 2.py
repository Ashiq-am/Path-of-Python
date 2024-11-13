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

insertQuery = " Select City, IF(City = 'Patna','True','False') from persons;"
mycursor.execute(insertQuery)
myresult = mycursor.fetchall()

print(myresult)

# close the Connection
db.close()
