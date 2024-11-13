import psycopg2

conn = psycopg2.connect(
	database="EMPLOYEE_DATABASE", user='postgres',
password='pass', host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''SELECT employee.empno,employee.ename,
dept.deptno from employee cross JOIN dept '''

cursor.execute(sql)
results = cursor.fetchall()
for i in results:
	print(i)
conn.commit()
conn.close()
