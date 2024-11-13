# import mysql.connector module
import mysql.connector

# establish connection
database = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="gfg"
)

# creating cursor object
cur_object = database.cursor()
print("like operator address has three letters only")

# query
find = "SELECT * from itdept where Address like '___' "

# execute the query
cur_object.execute(find)

# fetching all results
data = cur_object.fetchall()
for i in data:
	print(i[0], i[1], i[2], i[3], sep="--")

# close database connection
database.close()
