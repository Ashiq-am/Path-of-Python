import mysql.connector

mydb = mysql.connector.connect(
	host = 'localhost',
	database = 'employee',
	user = 'root',
	password = 'Your_pass'
)

cs = mydb.cursor()
statement = "INSERT INTO geekstudent( id, name,gender, subject) VALUES(6,'Shoit','M', 'ML')"
cs.execute(statement)
mydb.commit()

print(cs.rowcount, " record(s) added")

print(cs.lastrowid)
