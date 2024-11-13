""""""



'''
Fetching the data from record is simple as the inserting them. The execute method uses the SQL command 
of getting all the data from the table using “Select * from table_name” and all the table data can be fetched 
in an object in the form of list of lists.
'''




# Python code to demonstrate SQL to fetch data.

# importing the module
import sqlite3

# connect withe the myTable database
connection = sqlite3.connect("myTable.db")

# cursor object
crsr = connection.cursor()

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM emp")

# store all the fetched data in the ans variable
ans = crsr.fetchall()

# Since we have already selected all the data entries
# using the "SELECT *" SQL command and stored them in
# the ans variable, all we need to do now is to print
# out the ans variable
print(ans)













"""It should be noted that the database file that will be created will be in the same folder as that of the python file. 
If we wish to change the path of the file, change the path while opening the file."""