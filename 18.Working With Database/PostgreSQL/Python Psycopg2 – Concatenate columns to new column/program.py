import psycopg2

conn = psycopg2.connect(
	database="geeks", user='postgres',
	password='root', host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

# adding an extra column
sql ='''alter table employee add column empno_name varchar(30);'''
cursor.execute(sql)

# updating the new tables with values
sql1 = '''UPDATE employee SET empno_name = concat(empno, ename);'''

cursor.execute(sql1)

# printing out the concatenated column
sql2 = '''select empno_name from employee;'''
cursor.execute(sql2)
results = cursor.fetchall()
for i in results:
	print(i)
conn.commit()
conn.close()
