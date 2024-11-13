import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root",
	database="testdb"
)
# getting the cursor by cursor() method
mycursor = db.cursor()

insertQuery = "INSERT INTO Fruits (Fruit_name) VALUES ('Apple');"

mycursor.execute(insertQuery)

print("No of Record Inserted :", mycursor.rowcount)

# we can use the id to refer to that row later.
print("Inserted Id :", mycursor.lastrowid)

# To ensure the Data Insertion, commit database.
db.commit()

# close the Connection
db.close()
