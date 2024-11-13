import sqlite3

connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# WHERE CLAUSE TO RETRIEVE DATA
cursor.execute("SELECT * from STUDENT WHERE First_name Like'R%'")

# printing the cursor data
print(cursor.fetchall())

connection.commit()
connection.close()
