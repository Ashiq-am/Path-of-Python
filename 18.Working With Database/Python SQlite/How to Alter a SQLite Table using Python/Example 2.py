import sqlite3

# Connecting to sqlite
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Add a new column to geek table
new_column = "ALTER TABLE GEEK ADD COLUMN UserName CHAR(25)"

cursor_obj.execute(new_column)

# Display table
data = cursor_obj.execute("SELECT * FROM GEEK")
print('GEEK Table:')
for row in data:
	print(row)

connection_obj.commit()

# Close the connection
connection_obj.close()
