import psycopg2

conn = psycopg2.connect(
	database="geeks",
	user='postgres',
	password='pass',
	host='localhost',
	port= '5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''SELECT * FROM products'''


cursor.execute(sql)
column_names = [desc[0] for desc in cursor.description]
for i in column_names:
	print(i)
conn.commit()
conn.close()
