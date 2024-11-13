# importing packages
import psycopg2

# forming connection
conn = psycopg2.connect(
	database="Classroom",
user='postgres',
password='pass',
	host='127.0.0.1', port='5432'
)

conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

# list of rows to be inserted
sql = ''' create table Student_Details(student_id int, student_name varchar(30),
		cgpa decimal)'''

# executing sql statement
cursor.execute(sql)
print('Table successfully created')

# list of rows to be inserted
values = [(12891, 'rachel', 9.5), (12892, 'ross', 8.93),
		(12893, 'nick', 9.2)]

# executing the sql statement
cursor.executemany("INSERT INTO Student_Details1 VALUES(%s,%s,%s)", values)

# select statement to display output
sql1 = '''select * from Student_Details;'''

# executing sql statement
cursor.execute(sql1)

# fetching rows
for i in cursor.fetchall():
	print(i)

# commiting changes
conn.commit()

# closing connection
conn.close()
