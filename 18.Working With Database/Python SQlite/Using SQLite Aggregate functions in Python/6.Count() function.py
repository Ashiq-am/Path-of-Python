# import the sqlite module
import sqlite3

# establishing a connection to the database
connection = sqlite3.connect("sales.db")

# creating a cursor object
cursor = connection.cursor()

# count of all the rows of the database
count = "select count(*) from sales1"

cursor.execute(count)

print("The count of all rows of the table :")
print(cursor.fetchone()[0])

# Closing database connection
connection.close()
