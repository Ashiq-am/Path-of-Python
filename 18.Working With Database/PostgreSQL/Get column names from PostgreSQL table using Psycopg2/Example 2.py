import psycopg2

conn = psycopg2.connect(
	database="geeks",
	user='postgres',
	password='root',
	host='localhost',
	port='5432'
)

conn.autocommit = True


with conn:
	with conn.cursor() as cursor:
		cursor.execute(
			"select COLUMN_NAME from information_schema.columns\
			where table_name='products'")
		column_names = [row[0] for row in cursor]

print("Column names:\n")

for i in column_names:
	print(i)
