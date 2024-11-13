# Establish connection to MySQL database
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root123",
	database="geeks"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the query
query = "SELECT count(*) AS New_column_name FROM information_schema.columns where table_name = 'Persons';"
mycursor.execute(query)

myresult = mycursor.fetchall()

print(myresult[-1][-1])

# Close database connection
mydb.close()
