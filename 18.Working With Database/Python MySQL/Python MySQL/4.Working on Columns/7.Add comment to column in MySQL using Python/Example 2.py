# import required module
import pymysql

# establish connection connection
conn = pymysql.connect(host="localhost", user="root",
					password="1234",db="test")

# create cursor object
mycursor = conn.cursor()

# execute query
mycursor.execute("""ALTER TABLE geeksforgeeks MODIFY NAME CHAR(50) 
"COMMENT 'ENTER NAMES HERE',MODIFY ADDRESS CHAR(50) COMMENT 
'Do not Enter Address\nmore than 50 characters',
MODIFY AGE INT COMMENT 'Enter Age here',
MODIFY MOB_NUMBER INT COMMENT 'Mobile number should be of 10 digits', 
MODIFY ID_NO VARCHAR(50) COMMENT 'Id Number is Unique\nKindly Enter different Ids'""")

# display comments of all attributes
mycursor.execute("SHOW FULL COLUMNS FROM GEEKSFOEGEEKS")
result = mycursor.fetchall()
for i in result:
	print(i)
mycursor.execute("COMMIT")

# terminate connection
conn.close()
