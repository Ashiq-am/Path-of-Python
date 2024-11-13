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
statement ="SELECT * FROM STUDENT LIMIT 2"

cs.execute(statement)
result_set = cs.fetchall()

for x in result_set:
	print(x)
