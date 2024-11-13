# Import required packages
import mysql.connector

# Establish connection to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="geeksforgeeks",
    database="store"
)

# Create a cursor object
cursor = db.cursor()

# MySQL queries for copying existing table,
# selecting new table data and
# describing new table structure
queries = "CREATE TABLE inventory3 LIKE products; INSERT inventory3 SELECT * " \
          "FROM products; " \
          "DESC inventory3;"

# Execute the query
results = cursor.execute(queries, multi=True)

# Print data and description of newly created table
for result in results:
    if result.with_rows:
        for row in result:
            print(row)

        # Close database connection
db.close()
