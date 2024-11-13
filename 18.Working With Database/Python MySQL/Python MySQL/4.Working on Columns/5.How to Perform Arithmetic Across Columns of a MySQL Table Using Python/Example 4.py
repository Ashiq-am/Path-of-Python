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
mycursor = mydb.cursor( dictionary = True )

# MySQL query for getting halved selling price of all products
query = "SELECT selling_price, concat(selling_price / 2) AS discount_price " \
        "FROM product_info"

# Execute the query
mycursor.execute( query )

# Fetch result of query
myresult = mycursor.fetchall()

# Print result of query
print(f"SP \t Discounted Price")
for row in myresult:
    print(f"{ row[ 'selling_price' ]} \t { row ['discount_price']}")

# Close database connection
mydb.close()
