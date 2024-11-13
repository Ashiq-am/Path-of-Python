import psycopg2

# connection establishment
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='password',
	host='localhost',
	port='5432'
)

conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

# query to export table into csv
sql = '''COPY demo TO
		'C:\\Users\\DELL\\Downloads\\Exported_data.csv'
		DELIMITER ',' CSV HEADER'''

# executing above query
cursor.execute(sql)

# Closing the connection
conn.close()
