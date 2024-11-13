# import the sqlite module
import sqlite3

# establishing a connection to the database
connection = sqlite3.connect("sales.db")

# creating a cursor object
cursor = connection.cursor()

# sum of all the yearly sale
sum_yearly_sale = "select sum(yearly_sale) from sales1"

cursor.execute(sum_yearly_sale)

# Print the sum of scores
print("The sum of yearly sale is :")

print(cursor.fetchone()[0])

# Closing database connection
connection.close()
