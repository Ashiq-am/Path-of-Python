# importing packages
import psycopg2

# establishing connection
conn = psycopg2.connect(
	database="Employee_db", user='postgres',
	password='root', host='localhost', port='5432'
)

# setting autocommit to True
conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

sql = '''SELECT * FROM employee;'''

# executing the sql command
cursor.execute(sql)

# fetching all the rows
results = cursor.fetchall()
print(results)

# committing changes
conn.commit()

# closing connection
conn.close()
