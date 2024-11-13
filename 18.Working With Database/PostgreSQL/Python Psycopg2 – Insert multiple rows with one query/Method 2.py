# importing packages
import psycopg2

# forming connection
conn = psycopg2.connect(
	database="Classroom",
	user='postgres',
	password='pass',
	host='127.0.0.1',
	port='5432'
)

conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

# list of rows to be inserted

values = [(14, 'Ian', 78), (15, 'John', 88), (16, 'Peter', 92)]

# cursor.mogrify() to insert multiple values
args = ','.join(cursor.mogrify("(%s,%s,%s)", i).decode('utf-8')
				for i in values)

# executing the sql statement
cursor.execute("INSERT INTO classroom VALUES " + (args))

# select statement to display output
sql1 = '''select * from classroom;'''

# executing sql statement
cursor.execute(sql1)

# fetching rows
for i in cursor.fetchall():
	print(i)

# commiting changes
conn.commit()

# closing connection
conn.close()
