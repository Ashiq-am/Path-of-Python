# Establish connection to MySQL database
import mysql.connector

# give connection with xampp
database = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="sravan"
)

# Creating cursor object
cur_object = database.cursor()

find = "SELECT department,sum(strength) from college_data GROUP BY(department) HAVING sum(strength)<=400 "

# Execute the query
cur_object.execute(find)

# fetching all results
data = cur_object.fetchall()
print("Total departments with count less than 400 : ")
print(" ")
for res in data:
	print(res[0],res[1],sep="--")

# Close database connection
database.close()
