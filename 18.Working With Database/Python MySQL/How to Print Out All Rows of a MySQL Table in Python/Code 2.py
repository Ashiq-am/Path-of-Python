# import required modules
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

# connect python with mysql with your hostname,
# username, password and database
db = MySQLdb.connect("localhost", "root", "", "techgeeks")

# get cursor object
cursor = db.cursor()

# execute your query
cursor.execute("SELECT * FROM techcompanies")

# fetch all the matching rows
result = cursor.fetchall()

# loop through the rows
for row in result:
	print(row, '\n')
