import psycopg2

# Connection to the PostGreSql database
connection = psycopg2.connect(
	host="host_name",
	database="database_name",
	user="username",
	password="password"
)

# Creation of a cursor object
cursor = connection.cursor()

# Define the update statement with placeholders for dynamic data
update="UPDATE table_name SET column1 = %s, column2 = %s WHERE id = %s"

# Define the data to be updated
data = [
	(value1,value2,id1),
	(value1,value2,id2),
	(value1,value2,id3),
	# ...........
]

# Execute the update statement for each row of data
for row in data:
	cursor.execute(update,row)

# Commit the changes to the database
connection.commit()

# Close the cursor and database connection
cursor.close()
connection.close()
