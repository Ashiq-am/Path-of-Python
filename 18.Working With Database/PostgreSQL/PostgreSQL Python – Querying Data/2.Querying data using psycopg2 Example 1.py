# This program uses fetchall()
# to query all the records from a table

# GET THE CONNECTION OBJECT
conn = get_connection()

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()

# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM students;")

# FETCH ALL THE ROWS FROM THE CURSOR
data = curr.fetchall()

# PRINT THE RECORDS
for row in data:
	print(row)

# CLOSE THE CONNECTION
conn.close()
