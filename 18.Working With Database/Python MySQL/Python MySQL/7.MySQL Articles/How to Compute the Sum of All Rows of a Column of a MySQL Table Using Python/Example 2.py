# import required module
import mysql.connector

# connect python with mysql with your hostname,
# database, user and password
db = mysql.connector.connect(host='localhost',
							database='gfg',
							user='root',
							password='')

# create cursor object
cursor = db.cursor()

# get the sum of rows of a column
cursor.execute("SELECT SUM(members) FROM club")

# fetch sum and display it
print(cursor.fetchall()[0][0])

# terminate connection
db.close()
