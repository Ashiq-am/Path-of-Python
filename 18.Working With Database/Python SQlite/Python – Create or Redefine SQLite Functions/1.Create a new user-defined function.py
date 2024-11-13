import sqlite3

# define user defined function
def _customFun(fstring, dept):
	result = 'Welcome ' + fstring + ' your dept is ' + dept
	return result


# define connection and cursor
connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# create the user defined function
connection.create_function("ROHACK", 2, _customFun)

# create and execute sql query
sqlQuery = "select ROHACK(First_Name,Department) from " \
           "STUDENT where Student_ID = 1"
cursor.execute(sqlQuery)
print(*cursor.fetchone())

# close cursor and connection
cursor.close()
connection.close()
