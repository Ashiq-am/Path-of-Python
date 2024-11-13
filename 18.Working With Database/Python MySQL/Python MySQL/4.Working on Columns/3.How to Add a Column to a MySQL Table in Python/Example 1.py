# Import required packages
import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
	host = "localhost",
	user = "username",
	password = "geeksforgeeks",
	database = "College"
)

# Create a cursor object
mycursor = mydb.cursor()

# MySQL query for adding a column
query = ("ALTER TABLE students ADD stream VARCHAR(100) DEFAULT 'CS'")
# Execute the query
mycursor.execute(query)

# Print description of students table
mycursor.execute("desc students")
myresult = mycursor.fetchall()
for row in myresult:
	print(row)

# Close database connection
mydb.close()
