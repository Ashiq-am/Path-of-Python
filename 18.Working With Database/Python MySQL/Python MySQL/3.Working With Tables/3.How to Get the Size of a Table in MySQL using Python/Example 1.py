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
query = "SELECT table_name AS `Table`, round(((data_length + index_length) 1024 1024), 2) " \
        "`Size in MB` FROM information_schema.TABLES WHERE table_schema = 'Geeks' " \
        "AND table_name = 'Persons';"

mycursor.execute(query)

# Display size of each table
myresult = mycursor.fetchall()

for item in myresult:
	print(item[0], "Size in MB: ", item[-1])
