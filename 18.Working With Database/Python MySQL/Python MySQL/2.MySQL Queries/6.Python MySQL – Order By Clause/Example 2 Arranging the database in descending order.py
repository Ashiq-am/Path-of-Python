# Python program to demonstrate
# order by clause


import mysql.connector

# Connecting to the Database
mydb = mysql.connector.connect(
    host='localhost',
    database='College',
    user='root',
)

cs = mydb.cursor()

# Order by clause
statement = "SELECT * FROM Student ORDER BY Name DESC"
cs.execute(statement)

result_set = cs.fetchall()

for x in result_set:
    print(x)

# Disconnecting from the database
mydb.close()
