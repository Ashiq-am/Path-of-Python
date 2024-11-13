import sqlite3

# re-define existing SQLite function with
# new defination
def length(data):
	result = len(data) + 10
	return result


# define connection and cursor
connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# create the function with same name as existing function
connection.create_function("length", 1, length)

# create and execute sql query
sqlQuery = "select length(First_Name) from STUDENT where Student_ID = 1"
cursor.execute(sqlQuery)
print(*cursor.fetchone())

# close cursor and connection
cursor.close()
connection.close()
