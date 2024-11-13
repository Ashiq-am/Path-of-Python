import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()
cursor_obj.execute("SELECT * FROM GEEK")
print(cursor_obj.fetchall())

#delete data
'''It will delete all rows from
the table
'''
cursor_obj.execute("DELETE FROM GEEK")
print()
print("After deleting all rows")
cursor_obj.execute("SELECT * FROM GEEK")
print(cursor_obj.fetchall())
connection_obj.commit()
# Close the connection
connection_obj.close()
