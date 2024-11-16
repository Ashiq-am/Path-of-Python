# import packages
import psycopg2
import psycopg2.extras as extras
import pandas as pd


def execute_values(conn, df, table):

	tuples = [tuple(x) for x in df.to_numpy()]

	cols = ','.join(list(df.columns))

	# SQL query to execute
	query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
	cursor = conn.cursor()
	try:
		extras.execute_values(cursor, query, tuples)
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print("Error: %s" % error)
		conn.rollback()
		cursor.close()
		return 1
	print("execute_values() done")
	cursor.close()


# establishing connection
conn = psycopg2.connect(
	database="Airlines_Database",
	user='postgres',
	password='sherlockedisi',
	host='127.0.0.1',
	port='5432'
)
sql = '''CREATE TABLE airlines_final1(id int ,day
char(20) ,airline char(20),destination char(20));'''

# creating a cursor
cursor = conn.cursor()
cursor.execute(sql)
data = pd.read_csv("airlines_final.csv")

data = data[["id", "day", "airline", "destination"]]

# using the function defined
execute_values(conn, data, 'airlines_final1')
