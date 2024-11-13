# importing sqlite module
import sqlite3

# create connection to the database my_database
connection = sqlite3.connect('my_database.db')

# create table named address of customers
# with 4 columns id,name age and address
connection.execute('''CREATE TABLE ship (ship_id INT, ship_name \
TEXT NOT NULL, ship_destination CHAR(50) NOT NULL); ''')

print("Ship table created successfully")

# close the connection
connection.close()
