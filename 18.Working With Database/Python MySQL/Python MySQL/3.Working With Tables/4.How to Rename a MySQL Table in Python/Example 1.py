# Import required packages
import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
	host="localhost",
	user="username",
	password="geeksforgeeks",
	database="store"
)

# Create a cursor object
mycursor = mydb.cursor()

# MySQL query for for renaming a table
query = "ALTER TABLE staff RENAME to employees"
# Execute the query
mycursor.execute(query)

# Print names of all tables in the database
mycursor.execute("SHOW TABLES")
myresult = mycursor.fetchall()
for row in myresult:
	print(row)

# Close database connection
mydb.close()
