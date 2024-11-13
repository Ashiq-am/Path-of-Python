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
mycursor = mydb.cursor(dictionary = True )

# MySQL query for getting profit
# (i.e. selling price - cost price)
query = "SELECT selling_price, cost_price, concat(selling_price - cost_price) AS profit FROM product_info"

# Execute the query
mycursor.execute( query )

# Fetch result of query
myresult = mycursor.fetchall()

# Print result of query
print(f"SP \t CP \t Profit")
for row in myresult:
    print(f"{ row[ 'selling_price' ]} \t { row[ 'cost_price' ]} \t { row[ 'profit' ]}")

mydb.close()
