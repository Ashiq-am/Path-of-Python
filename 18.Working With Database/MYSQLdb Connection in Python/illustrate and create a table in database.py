# Python code to illustrate and create a
# table in database
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","testpassword","gfgdb" )

cursor = db.cursor()

# Drop table if it already exist using execute()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE ( 
		FNAME CHAR(20) NOT NULL, 
		LNAME CHAR(20), 
		AGE INT )"""

cursor.execute(sql) #table created

# disconnect from server
db.close()
