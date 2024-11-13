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

# query to count total number of rows
sql = 'SELECT count(*) from products;'
data=[]

# execute the query
cursor.execute(sql,data)
results = cursor.fetchone()

#loop to print all the fetched details
for r in results:
    print(r)
print("Total number of rows in the table:", r)

# query to count number of rows
# where country name is India
sql1 = 'SELECT count(*) from products WHERE "price" = 1.99;'
data1=['India']

# execute query
cursor.execute(sql1,data1)
result = cursor.fetchone()
for r1 in result:
    print(r1)
print("Total Number of rows where country name is India:",r1)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
