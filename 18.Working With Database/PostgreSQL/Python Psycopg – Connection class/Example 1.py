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
