# import the sqlite module
import sqlite3

# establishing a connection to the database
connection = sqlite3.connect("sales.db")

# creating a cursor object
cursor = connection.cursor()

# total monthly_sale
Total_mon_sale= "select total(monthly_sale) from sales1"
cursor.execute(Total_mon_sale)

# Print the total score
print("The total monthly sale of all items is:")

print(cursor.fetchone()[0])

# Closing database connection
connection.close()
