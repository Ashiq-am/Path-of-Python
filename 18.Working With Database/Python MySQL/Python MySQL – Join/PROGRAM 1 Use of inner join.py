import mysql.connector

# Conencting to the database
mydb = mysql.connector.connect(
host ='localhost',
database ='College',
user ='root',
)

cs = mydb.cursor()

# STUDENT and STudent are
# two different database
statement ="SELECT S.NAME from Student S JOIN Student on S.Roll_no = Student.Roll_no"

cs.execute(statement)
result_set = cs.fetchall()

for x in result_set:
	print(x)
