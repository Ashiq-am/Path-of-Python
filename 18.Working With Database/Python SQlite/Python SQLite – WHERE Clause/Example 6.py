import sqlite3

connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# WHERE CLAUSE TO DELETE DATA
cursor.execute("DELETE from STUDENT WHERE Age = 32")

#printing the cursor data
cursor.execute("SELECT * from STUDENT")
print(cursor.fetchall())

connection.commit()
connection.close()
