# Import required module
import mysql.connector

# Establish connection
# to MySQL database
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root123",
	database="geeks")

# Create cursor object
mycursor = mydb.cursor()

# Execute query
query = "SELECT TABLE_NAME AS `Table`, ROUND(((DATA_LENGTH + INDEX_LENGTH) " \
        "1024 1024),2) AS `Size (MB)` FROM information_schema.TABLES " \
        "WHERE TABLE_SCHEMA = 'Geeks' ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC"

mycursor.execute(query)

# Display size of each table
myresult = mycursor.fetchall()

for item in myresult:
	print(item[0], "Size in MB: ", item[-1])
