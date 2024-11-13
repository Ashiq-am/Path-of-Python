import datetime
import sqlite3

# make a database connection and cursor object
connection = sqlite3.connect('StudentAssignment.db',
							detect_types=sqlite3.PARSE_DECLTYPES |
							sqlite3.PARSE_COLNAMES)
cursor = connection.cursor()

# select query to retrive data
cursor.execute("SELECT * from ASSIGNMENT where StudentId = 2")
fetchedData = cursor.fetchall()

# to access specific fetched data
for row in fetchedData:
	StudentID = row[0]
	StudentName = row[1]
	SubmissionDate = row[2]
	print(StudentName, ", ID -",
		StudentID, "Submitted Assignments")
	print("Date and Time : ",
		SubmissionDate)
	print("Submission date type is",
		type(SubmissionDate))

# commit the changes,
# close the cursor and database connection
cursor.close()
connection.close()
