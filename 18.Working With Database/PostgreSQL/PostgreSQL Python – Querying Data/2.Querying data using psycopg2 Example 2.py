# This program uses fetchone() to
# query one by one record from a table

# GET THE CONNECTION OBJECT
conn = get_connection()

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()

# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM students;")

# FETCH THE FIRST ROW FROM THE CURSOR
data1 = curr.fetchone()
print(data1)

# FETCH THE SECOND ROW FROM THE CURSOR
data2 = curr.fetchone()
print(data2)

# CLOSE THE CONNECTION
conn.close()
