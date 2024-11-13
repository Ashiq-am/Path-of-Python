# Import required packages
import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
host = "localhost" ,
user = "username" ,
password = "geeksforgeeks" ,
database = "grocery"
)

# MySQLCursorDict creates a cursor that returns rows as dictionaries
mycursor = mydb.cursor(dictionary = True)

# MySQL query for getting total amount (i.e. sale amount * quantity)
query = """SELECT selling_price, tax, concat((selling_price * tax)) 
             AS total_amount FROM product_info"""

# Execute the query
mycursor.execute( query )

# Fetch result of query
myresult = mycursor.fetchall()

# Print result of query
print(f"SP \t Tax \t Total")
for row in myresult:
    print(f"{row[ 'selling_price' ]} \t { row[ 'tax' ]}\t{row['total_amount']}")

# Close database connection
mydb.close()
