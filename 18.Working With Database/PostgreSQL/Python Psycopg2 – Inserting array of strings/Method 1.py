# importing packages
import psycopg2

# forming connection
conn = psycopg2.connect(
	database="Classroom",
	user='postgres',
	password='sherlockedisi',
	host='127.0.0.1',
	port='5432'
)

conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

# list of rows to be inserted
values = [17, 'samuel', 95]

# executing the sql statement
cursor.execute("INSERT INTO classroom VALUES(%s,%s,%s) ", values)

# select statement to display output
sql1 = '''select * from classroom;'''

# executing sql statement
cursor.execute(sql1)

# fetching rows
for i in cursor.fetchall():
	print(i)

# committing changes
conn.commit()

# closing connection
conn.close()
