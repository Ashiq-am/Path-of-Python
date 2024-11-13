# import reqired module
import pymysql

# establish connection to MySQL
connection = pymysql.connect(

    # specify host
    host='localhost',

    # specify root account
    user='root',

    # specify password for root account
    password='1234',

    # default port number is 3306 fro MySQL
    port=3306
)

# make a cursor to run sql queries
mycursor = connection.cursor()

# granting all permissions on all databases and their
# tables of geeksforgeeks user permission also includes
# table and column grants
mycursor.execute("Grant all on *.* to geeksforgeeks@localhost")

# print all privileges of geeksforgeeks user
mycursor.execute("Show grants for geeksforgeeks@localhost")
result = mycursor.fetchall()
print(result)

# commit privileges
mycursor.execute("Flush Privileges")

# close connection to MySQL
connection.close()
