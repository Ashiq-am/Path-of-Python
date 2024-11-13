# importing packages
import psycopg2

# forming the connection
conn = psycopg2.connect(
	database="Hospital_database", user='postgres',
	password='pass', host='127.0.0.1', port='5432'
)

# Setting auto commit to True
conn.autocommit = True

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()
