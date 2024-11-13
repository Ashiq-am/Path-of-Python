# importing sqlite3 module
import sqlite3

# create connection by using object
# to connect with college_details
# database
connection = sqlite3.connect('college.db')

# sqlite execute query to insert a table
connection.execute(
	'''insert into college values ( '7058', 'sravan kumar','hyd' )''')
connection.execute(
	'''insert into college values ( '7059', 'jyothika','tenali' )''')
connection.execute(
	'''insert into college values ( '7072', 'harsha verdhan','nandyal' )''')
connection.execute(
	'''insert into college values ( '7099', 'virinchi','Guntur' )''')

# sqlite execute query to display data
# in the college
a = connection.execute("select * from college")

# fetch all records
print(a.fetchall())

# terminate the connection
connection.close()
