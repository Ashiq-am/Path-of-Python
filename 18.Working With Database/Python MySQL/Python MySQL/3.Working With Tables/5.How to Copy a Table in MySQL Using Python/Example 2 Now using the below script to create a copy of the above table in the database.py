# import required modules
import pymysql

# connect python with mysql with your hostname,
# username, password and database
connection= pymysql.connect("localhost", "root", "", "geek")

# make a cursor
mycursor = connection.cursor()

# create a new table and copy all records from
# previous table into the newly created table
mycursor.execute("create table geeksdemocopy select * from geeksdemo")

# list all the tables
mycursor.execute("Show tables")

# fetchall() will store all the names of tables into query1
query1 = mycursor.fetchall()

# print name of tables
for i in query1:
	print(i)

# read all records from copy table
mycursor.execute("Select * from geeksdemocopy")

# fetchall() will store all the records of copy table into query2
query2 = mycursor.fetchall()

# print all records
for i in query2:
	print(i)
