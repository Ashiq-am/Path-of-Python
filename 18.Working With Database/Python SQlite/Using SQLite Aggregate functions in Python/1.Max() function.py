# import the sqlite module
import sqlite3

# establishing a connection to the database
connection = sqlite3.connect("sales.db")

# Obtain a cursor object
cursor = connection.cursor()

# Find the maximum yearly_sale
max_sale = "select max(yearly_sale) from sales1"

cursor.execute(max_sale)

print("The maximum yearly sale is is:")
print(cursor.fetchone()[0])

# Closing database connection
connection.close()
