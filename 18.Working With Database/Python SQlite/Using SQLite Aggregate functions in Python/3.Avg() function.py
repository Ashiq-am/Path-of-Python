# import the sqlite module
import sqlite3

# establishing a connection to the database
connection = sqlite3.connect("sales.db")

# creating a cursor object
cursor = connection.cursor()

# average value of yearly_sales
avg_sale = "select avg(yearly_sale) from sales1"

cursor.execute(avg_sale)

print("The average yearly sales is:")

print(cursor.fetchone())
# Closing database connection
connection.close()
