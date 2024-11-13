# Python program to demonstrate
# commit() method


import mysql.connector

# Connecting to the Database
mydb = mysql.connector.connect(
host ='localhost',
database ='College',
user ='root',
)

cs = mydb.cursor()

# drop clause
statement ="UPDATE STUDENT SET AGE = 23 WHERE Name ='Rishi Kumar'"

cs.execute(statement)

# commit changes to the database
mydb.commit()

# Disconnecting from the database
mydb.close()
