import psycopg2.extras

conn = psycopg2.connect(
	database="codes", user='postgres', password='pass',
	host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
sql = '''CREATE TABLE continent_codes(code varchar(3), name char(20),
concatenated_column varchar(30));'''


cursor.execute(sql)

sql2 = '''COPY continent_codes(code,name,
concatenated_column)
FROM '/private/tmp/continent_codes.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql2)

sql3 = '''select * from continent_codes;'''
cursor.execute(sql3)
results = cursor.fetchall()
for row in results:
	print("code: {}".format(row['code']))
	print("name: {}".format(row['name']))
	print("concatenated_column: {}".format(row['concatenated_column']))
conn.commit()
conn.close()
