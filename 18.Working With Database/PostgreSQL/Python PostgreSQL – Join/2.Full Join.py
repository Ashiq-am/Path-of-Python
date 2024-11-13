import psycopg2

conn = psycopg2.connect(
	database="EMPLOYEE_DATABASE", user='postgres',
password='pass', host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''SELECT * from employee FULL JOIN dept\
ON employee.deptno =dept.deptno '''

cursor.execute(sql)
results = cursor.fetchall()
for i in results:
	print(i)
conn.commit()
conn.close()
