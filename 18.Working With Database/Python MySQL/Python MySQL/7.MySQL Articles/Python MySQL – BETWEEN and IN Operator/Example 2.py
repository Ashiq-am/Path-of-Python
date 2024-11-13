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

# query
print("in operator demo")
find = "SELECT cus_id,purchase from geeks where purchase in (67) "

# Execute the query
cur_object.execute(find)

# fetching all results
data = cur_object.fetchall()
print("customer id with purchase 67: ")
print(" ")

for res in data:
	print(res[0], res[1], sep="--")
print(" ")
print("not in operator demo")
print(" ")

find = "SELECT cus_id,purchase from geeks where purchase not in (67) "

# Execute the query
cur_object.execute(find)

# fetching all results
data = cur_object.fetchall()
print(" ")
print("custmer id with purchase except 67 purchase ")
print(" ")

for res in data:
	print(res[0], res[1], sep="--")

# Close database connection
database.close()
