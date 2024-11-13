# importing packages
import psycopg2

# forming connection
conn = psycopg2.connect(
	database="Classroom",
	user='postgres',
	password='pass',
	host='127.0.0.1',
	port='5432'
)
conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

# sql statement to be executed
sql = '''insert into classroom(enrollment_no, name , science_marks)
values(12, 'sarah', 90),(13,'Ray',81); '''

# executing the sql statement
cursor.execute(sql)

# select statement to display output
sql1 = '''select * from classroom;'''

# executing sql statement
cursor.execute(sql1)

# fetching rows
for i in cursor.fetchall():
	print(i)

# commiting changes
conn.commit()

# closing connection
conn.close()
