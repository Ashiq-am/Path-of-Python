import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
table = """ CREATE TABLE GEEK (
			Email VARCHAR(255) NOT NULL,
			First_Name CHAR(25) NOT NULL,
			Last_Name CHAR(25),
			Score INT
		); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the coonection
connection_obj.close()
