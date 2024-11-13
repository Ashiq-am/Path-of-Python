import psycopg2

conn = psycopg2.connect(
	database="geeks", user='postgres',
password='root', host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE employees(emp_id int,emp_name varchar, \
salary decimal); '''

cursor.execute(sql)

conn.commit()
conn.close()
