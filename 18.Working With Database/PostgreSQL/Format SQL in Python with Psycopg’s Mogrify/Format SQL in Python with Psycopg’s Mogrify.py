# importing packages
import psycopg2

# forming connection
conn = psycopg2.connect(
	database="Emp_database",
	user='postgres',
	password='pass',
	host='127.0.0.1',
	port='5432'
)

conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

cursor.execute(
	'create table emp_table(emp_code int,\
	emp_name varchar(30), emp_salary decimal)')

# list of rows to be inserted

values = [(34545, 'samuel', 48000.0),
		(34546, 'rachel', 23232),
		(34547, 'Sean', 92000.0)]

# cursor.mogrify() to insert multiple values
args = ','.join(cursor.mogrify("(%s,%s,%s)", i).decode('utf-8')
				for i in values)

# executing the sql statement
cursor.execute("INSERT INTO emp_table VALUES " + (args))

# select statement to display output
sql1 = '''select * from emp_table;'''

# executing sql statement
cursor.execute(sql1)

# fetching rows
for i in cursor.fetchall():
	print(i)

# commiting changes
conn.commit()

# closing connection
conn.close()
