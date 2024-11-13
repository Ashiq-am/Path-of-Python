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
cursor.execute("SELECT * FROM Documentary GROUP BY Name, Production HAVING COUNT(*) > 1;")

# fetch duplicate rows and display them
print('Duplicate Rows:')
for row in cursor.fetchall(): print(row)

# terminate connection
db.close()
