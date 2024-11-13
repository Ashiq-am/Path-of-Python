# import required modules
import pymysql

# establish connection to SQL database
connection = pymysql.connect(

    # specify hostname
    host="localhost",

    # specify user of mysql database
    user="root",

    # specify password for above user
    password="1234",

    # default port number for mysql is 3306
    port=3306,

    # specify database name on which you want to work
    db="test"
)

# make a cursor
mycursor = connection.cursor()

# create a new table geeksforgeekscopy and copy all
# records from geeksfoegeeks into the newly created table
mycursor.execute("create table geeksforgeekscopy select * from geeksfoegeeks")

# list all the tables
mycursor.execute("Show tables")

# fetchall() will store all the names
# of tables into query1
query1 = mycursor.fetchall()

# print name of tables
for i in query1:
    print(i)

# read all records from copy table
mycursor.execute("Select * from geeksforgeekscopy")

# fetchall() will store all the records
# of copy table into query2
query2 = mycursor.fetchall()

# print all records
for i in query2:
    print(i)
