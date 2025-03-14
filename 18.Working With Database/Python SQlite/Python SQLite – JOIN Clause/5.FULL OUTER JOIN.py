# Import required libraries
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect(r'C:\Users\SQLite\Geeks.db')

# Create cursor object
cursor = conn.cursor()

# Query for FULL OUTER JOIN
sql = '''SELECT StudentID, StudentName, AdvisorName
FROM Student
LEFT JOIN Advisor
USING(AdvisorID)
UNION ALL
SELECT StudentID, StudentName, AdvisorName
FROM Advisor
LEFT JOIN Student
USING(AdvisorID)
WHERE Student.AdvisorID IS NULL;'''

# Executing the query
cursor.execute(sql)

# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
	print(row)

# Closing the connection
conn.close()
