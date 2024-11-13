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
print("like operator address starts with G")

# query
find = "SELECT * from itdept where Address like 'G%' "

# execute the query
cur_object.execute(find)

# fetching all results
data = cur_object.fetchall()
for i in data:
	print(i[0], i[1], i[2], i[3], sep="--")

# Close database connection
database.close()
