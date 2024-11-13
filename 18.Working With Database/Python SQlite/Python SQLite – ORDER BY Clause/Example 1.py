# importing sqlite module
import sqlite3

# create connection to the database
# geeks_database
connection = sqlite3.connect('geeks_database.db')

# create table named address of customers
# with 4 columns id,name age and address
connection.execute('''CREATE TABLE customer_address
		(ID INT PRIMARY KEY	 NOT NULL,
		NAME		 TEXT NOT NULL,
		AGE		 INT	 NOT NULL,
		ADDRESS	 CHAR(50)); ''')

# close the connection
connection.close()
