# Python program to demonstrate
# update clause


import mysql.connector

# Connecting to the Database
mydb = mysql.connector.connect(
host ='localhost',
database ='College',
user ='root',
)

cs = mydb.cursor()

# drop clause
statement ="UPDATE STUDENT SET Name = 'S.K. Anirban' WHERE Name ='SK Anirban'"

cs.execute(statement)
mydb.commit()

# Disconnecting from the database
mydb.close()
