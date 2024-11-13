# import the sqlite module
import sqlite3

# establishing a connection to the database
connection = sqlite3.connect("sales.db")

# Obtain a cursor object
cursor = connection.cursor()

# minimum yearly sale
min_sale = "select min(yearly_sale) from sales1"

cursor.execute(min_sale)

# Print the minimum score
print("The minimum yearly sale is:")

# fetching the result
print(cursor.fetchone()[0])

# Closing database connection
connection.close()
