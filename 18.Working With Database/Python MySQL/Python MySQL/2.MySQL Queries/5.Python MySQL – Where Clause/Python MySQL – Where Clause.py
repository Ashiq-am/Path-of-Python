import mysql.connector

#Establishing connection
conn = mysql.connector.connect(user='your_username',
							host='localhost',
							password ='your_password',
							database='College')

# Creating a cursor object using
# the cursor() method
mycursor = conn.cursor()

# SQL Query
sql = "select * from Student where Roll_no >= 3"

# Executing query
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)

# Closing the connection
conn.close()
