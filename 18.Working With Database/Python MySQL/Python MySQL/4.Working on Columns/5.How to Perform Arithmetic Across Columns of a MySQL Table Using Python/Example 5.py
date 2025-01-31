# Import required packages
import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
host = "localhost" ,
user = "username" ,
password = "geeksforgeeks" ,
database = "grocery"
)

# MySQLCursorDict creates a cursor
# that returns rows as dictionaries
mycursor = mydb.cursor(dictionary = True)

# MySQL query for getting remainder
query = "SELECT selling_price, cost_price, concat(selling_price % cost_price) AS mod_example FROM product_info"

# Execute the query
mycursor.execute( query )

# Fetch result of query
myresult = mycursor.fetchall()

# Print result of query
print(f"SP \t Qnty \t MOD")
for row in myresult:
    print(f"{ row [ 'selling_price' ]} \t { row [ 'cost_price' ]} \t{row[ 'mod_example' ]}")

# Close database connection
mydb.close()
