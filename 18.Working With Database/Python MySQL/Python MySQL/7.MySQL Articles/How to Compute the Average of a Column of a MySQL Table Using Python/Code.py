import mysql.connector

# database connection
connection = mysql.connector.connect(
	host="localhost", user="root",
	password="", database="school")
cursor = connection.cursor()

# queries for retrievint all rows
retrieve = "Select AVG(Marks) AS average from students;"

# executing the queries
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
	print("Average marks is :" + str(i[0]))


# commiting the connection then closing it.
connection.commit()
connection.close()
