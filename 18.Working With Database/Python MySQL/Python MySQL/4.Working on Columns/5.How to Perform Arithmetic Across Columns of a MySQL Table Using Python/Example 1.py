# Import required packages
import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="geeksforgeeks",
    database="grocery"
)

# MySQLCursorDict creates a cursor
# that returns rows as dictionaries
mycursor = mydb.cursor(dictionary=True)

# MySQL query for getting total
# sale amount (i.e. selling price + tax)
query = "SELECT Selling_price, tax, concat(Selling_price + tax) AS sale_amount FROM product"

# Execute the query
mycursor.execute(query)
# Fetch result of query
myresult = mycursor.fetchall()

# Print result of query
print(f"SP \t Tax \t Sale Amount")

for row in myresult:
    # Each value printed for display purpose (you can simply print row)
    print(f"{row['Selling_price']} \t {row['tax']} \t {row['sale_amount']}")

mydb.close()
