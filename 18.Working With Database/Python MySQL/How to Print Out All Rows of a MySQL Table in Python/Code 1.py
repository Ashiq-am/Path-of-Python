# import required modules
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

# connect python with mysql with your hostname,
# username, password and database
db= MySQLdb.connect("localhost", "root", "", "GEEK")

# get cursor object
cursor= db.cursor()

# execute your query
cursor.execute("SELECT * FROM geeksdemo")

# fetch all the matching rows
result = cursor.fetchall()

# loop through the rows
for row in result:
	print(row)
	print("\n")
