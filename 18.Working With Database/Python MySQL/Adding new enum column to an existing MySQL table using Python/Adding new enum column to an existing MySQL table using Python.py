# Establish connection to MySQL database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rot23",
    database="geeks"
)

# getting the cursor by cursor() method
mycursor = db.cursor()

query = "ALTER TABLE store ADD Department ENUM('Sweet','Snaks');"

mycursor.execute(query)

mycursor.execute(" desc store;")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

db.commit()

# close the Connection
db.close()
