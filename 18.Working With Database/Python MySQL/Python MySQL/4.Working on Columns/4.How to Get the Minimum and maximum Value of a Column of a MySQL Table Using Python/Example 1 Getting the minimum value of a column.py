# Establish connection to MySQL database
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root123",
database = "geeks"
)

# Create a cursor object
cursor = mydb.cursor()

# Execute the query
cursor.execute("SELECT MIN(Value) AS minimum FROM salary")

result = cursor.fetchall()

for i in result:
	maximum= float(i[0])
	print(maximum)

# Close database connection
mydb.close()
