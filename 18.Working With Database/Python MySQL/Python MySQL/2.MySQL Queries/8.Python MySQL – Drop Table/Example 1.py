# Python program to demonstrate
# drop clause


import mysql.connector

# Connecting to the Database
mydb = mysql.connector.connect(
    host='localhost',
    database='College',
    user='root',
)

cs = mydb.cursor()

# drop clause
statement = "Drop Table if exists Employee"

# Uncommenting statement ="DROP TABLE employee"
# Will raise an error as the table employee
# does not exists

cs.execute(statement)

# Disconnecting from the database
mydb.close()
