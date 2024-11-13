# import required modules
import pymysql

# establish connection to MySQL
connection = pymysql.connect(
    # specify host name
    host="localhost",

    # specify username
    user="root",

    # enter password for above user
    password="",

    # default port number for MySQL is 3306
    port=3306,

    # specify database name
    db="geek"
)

# make cursor for establish connection
mycursor = connection.cursor()

# display records before inserting
mycursor.execute("Select * from geeksdemo")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

# statement to insert record
mycursor.execute(
    "Insert into geeksdemo(id,name,gender,dept) \
select * from( Select 5,'Thomas','m','information technology') as temp \
    where not exists \
    (Select id from geeksdemo where id=5) LIMIT 1")
print("After inserting a record....")

# print records after insertion
mycursor.execute("Select * from geeksdemo")

myresult = mycursor.fetchall()
for i in myresult:
    print(i)
mycursor.execute("Commit")

# close connection
connection.close()
