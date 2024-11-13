# This program uses fetchmany()
# to query specified number of records from a table

# GET THE CONNECTION OBJECT
conn = get_connection()

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()

# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM students;")

print("First two records:")

# GET FIRST TWO RECORDS FROM DATABASE TABLE
data1 = curr.fetchmany(2)
for row in data1:
	print(row)

print("Next three records:")

# GET NEXT THREE RECORDS FROM DATABASE TABLE
data2 = curr.fetchmany(3)
for row in data2:
	print(row)

# CLOSE THE CONNECTION
conn.close()
