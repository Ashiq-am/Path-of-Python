import psycopg2

conn = psycopg2.connect(
	database="geeks", user='postgres',
	password='root', host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''insert into employee values('191351','divit','100000.0'),
									('191352','rhea','70000.0');
'''

cursor.execute(sql)

conn.commit()
conn.close()
