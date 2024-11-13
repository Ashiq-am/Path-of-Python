# Import required libraries
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect(r'C:\Users\SQLite\Geeks.db')

# Create cursor object
cursor = conn.cursor()

# Query for INNER JOIN
sql = '''SELECT StudentID, StudentName, AdvisorName
FROM Student
INNER JOIN Advisor
ON Student.AdvisorID = Advisor.AdvisorID;'''

# Executing the query
cursor.execute(sql)

# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
	print(row)

# Closing the connection
conn.close()
