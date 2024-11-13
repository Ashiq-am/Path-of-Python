# importing psycopg2
import psycopg2

conn=psycopg2.connect(
	database="geeks",
	user="postgres",
	password="root",
	host="localhost",
	port="5432"
)


# Creating a cursor object using the cursor()
# method
cursor = conn.cursor()

# drop table accounts
sql = '''DROP table IF EXISTS accounts '''

# Executing the query
cursor.execute(sql)

print("Table dropped !")
# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
