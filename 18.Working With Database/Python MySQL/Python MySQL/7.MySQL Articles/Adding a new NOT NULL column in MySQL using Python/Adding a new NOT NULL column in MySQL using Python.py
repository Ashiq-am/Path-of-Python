# Establish connection to MySQL database
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root123",
database = "geeks"
)

# getting the cursor by cursor() method
mycursor = db.cursor()

query = "ALTER TABLE employee ADD Place varchar(255) not null;"
query_1 = "insert into employee value('Rahul', 'Kumar', 25, 'M', '5999','98347000', 'Delhi');"

mycursor.execute(query)
mycursor.execute(query_1)

mycursor.execute("select * from employee;")
myresult = mycursor.fetchall()
for row in myresult:
	print(row)
db.commit()

# close the Connection
db.close()
