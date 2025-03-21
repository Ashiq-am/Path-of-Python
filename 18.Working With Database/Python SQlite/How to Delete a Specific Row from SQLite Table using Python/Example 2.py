# import sqlite module database
import sqlite3

# create connection to the database
# my_database
connection = sqlite3.connect('my_database.db')

# insert query to insert values
connection.execute("INSERT INTO ship VALUES (1, 'tata-hitachi','noida' )")
connection.execute("INSERT INTO ship VALUES (2, 'tata-mumbai','mumbai' )")
connection.execute("INSERT INTO ship VALUES (3, 'tata-express','hyderabad' )")

# query to display all data in the table
cursor = connection.execute("SELECT * from ship")
print("Actual data")

# display row by row
for row in cursor:
	print(row)

# query to delete all data where ship_id = 2
connection.execute("DELETE from ship where ship_id=2")

print("After deleting ship id = 2 row")

# display row by row
cursor = connection.execute("SELECT * from ship")
for row in cursor:
	print(row)

# close the connection
connection.close()
