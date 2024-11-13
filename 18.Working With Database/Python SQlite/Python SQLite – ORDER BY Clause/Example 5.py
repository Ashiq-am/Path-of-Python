# importing sqlite module
import sqlite3

# create connection to the database
# geeks_database
connection = sqlite3.connect('geeks_database.db')

# sql query to display name and id based
# on name in descending order
cursor = connection.execute(
	"SELECT NAME,ID from customer_address ORDER BY NAME DESC")

# display data row by row
for i in cursor:
	print(i)

# close the connection
connection.close()
