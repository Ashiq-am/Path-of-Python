import sqlite3

connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# WHERE CLAUSE TO RETRIEVE DATA
cursor.execute("SELECT * FROM STUDENT WHERE Department = 'IT'")

# printing the cursor data
print(cursor.fetchall())

connection.commit()
connection.close()
