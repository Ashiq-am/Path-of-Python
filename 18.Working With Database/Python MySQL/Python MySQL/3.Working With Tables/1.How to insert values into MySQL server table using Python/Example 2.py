import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root",
	database="testdb"
)

#getting the cursor by cursor() method
mycursor = db.cursor()

insertQuery = '''INSERT INTO 
			Fruits (Fruit_name, Taste, Production_in ) 
			VALUES ('Banana','Sweet',210);'''

mycursor.execute(insertQuery)

print("No of Record Inserted :", mycursor.rowcount)

# To ensure the data insertion, Always commit to the database.
db.commit()

# close the Connection
db.close()
