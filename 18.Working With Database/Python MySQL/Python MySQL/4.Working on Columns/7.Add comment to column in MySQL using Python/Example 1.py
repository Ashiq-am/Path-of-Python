# import required module
import pymysql

# make connection
conn = pymysql.connect(host="localhost", user="root",
					password="1234",db="test")

# create cursor object
mycursor = conn.cursor()

# execute query
mycursor.execute("ALTER TABLE geeksforgeeks MODIFY name "
                 "CHAR(50) COMMENT 'ENTER NAMES HERE'")

# display comments of all columns
mycursor.execute("SHOW FULL COLUMNS FROM GEEKSFOEGEEKS")
result = mycursor.fetchall()
for i in result:
	print(i)
mycursor.execute("COMMIT")

#terminate connection
conn.close()
