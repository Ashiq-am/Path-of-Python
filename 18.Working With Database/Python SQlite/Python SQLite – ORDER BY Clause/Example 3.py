# importing sqlite module
import sqlite3

# create connection to the database
# geeks_database
connection = sqlite3.connect('geeks_database.db')

# sql query to display all details from
# table in ascending order based on address.
cursor = connection.execute(
	"SELECT ADDRESS,ID from customer_address ORDER BY address DESC")

# display data row by row
for i in cursor:
	print(i)

# close the connection
connection.close()
