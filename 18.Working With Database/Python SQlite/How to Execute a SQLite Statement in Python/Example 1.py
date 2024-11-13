# importing sqlite3 module
import sqlite3

# create connection by using object to
# connect with college_details database
connection = sqlite3.connect('college.db')


# sqlite execute query to create a table
connection.execute("""create table college(
		geek_id,
		geek_name,
		address
	);""")

print("Table created successfully")

# terminate the connection
connection.close()
