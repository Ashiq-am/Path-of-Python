import psycopg2

conn = psycopg2.connect(
	database="classroom_database",
	user='postgres', password='pass',
	host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()


sql = ''' update student_details set
		cgpa = 9.5 ,
		branch = 'AE'
		where student_name = 'rahul';'''

cursor.execute(sql)

sql1 = '''select * from student_details;'''
cursor.execute(sql1)

for i in cursor.fetchall():
	print(i)

conn.commit()
conn.close()
