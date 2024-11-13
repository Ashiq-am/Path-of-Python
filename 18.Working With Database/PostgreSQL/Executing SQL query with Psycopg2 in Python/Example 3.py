import psycopg2

conn = psycopg2.connect(
	database="geeks", user='postgres',
	password='root', host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''SELECT * FROM employee;'''

cursor.execute(sql)
results = cursor.fetchall()
print(results)

conn.commit()
conn.close()
