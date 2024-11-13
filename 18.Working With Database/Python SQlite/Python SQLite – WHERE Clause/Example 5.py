import sqlite3

connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# WHERE CLAUSE TO UPDATE DATA
cursor.execute("UPDATE STUDENT SET Department ='E&TC' WHERE Student_ID = 2")

# printing the cursor data
cursor.execute("SELECT * from STUDENT")
print(cursor.fetchall())

connection.commit()
connection.close()
