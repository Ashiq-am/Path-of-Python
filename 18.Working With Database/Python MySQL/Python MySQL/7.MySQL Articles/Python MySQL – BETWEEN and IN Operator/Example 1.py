# Import mysql.connector module
import mysql.connector

# give connection with xampp
database = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="gfg"
)

# Creating cursor object
cur_object = database.cursor()
print("between operator demo")

# query
find = "SELECT cus_id,purchase from geeks where purchase between 10 and 100 "

# Execute the query
cur_object.execute(find)

# fetching results
data = cur_object.fetchall()
print(" ")
print("Purchase between 10 to 100 ")
print(" ")

for res in data:
	print(res[0], res[1], sep="--")
print(" ")

# Close database connection
database.close()
