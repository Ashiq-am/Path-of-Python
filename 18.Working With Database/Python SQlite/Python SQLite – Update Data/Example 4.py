# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('gfg4.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE STAFF(NAME VARCHAR(255), AGE int,
DEPARTMENT VARCHAR(255));"""
cursor.execute(table)

# Queries to INSERT records.
cursor.execute('''INSERT INTO STAFF VALUES('Anand', 45, 'Chemistry')''')
cursor.execute('''INSERT INTO STAFF VALUES('Ravi', 32, 'Physics')''')
cursor.execute('''INSERT INTO STAFF VALUES('Chandini', 32, 'Computer')''')
cursor.execute('''INSERT INTO STAFF VALUES('Latika', 40, 'Maths')''')

# Display data inserted
print("STAFF Table: ")
data = cursor.execute('''SELECT * FROM STAFF''')
for row in data:
    print(row)

# Updating
cursor.execute('''UPDATE STAFF SET NAME = 'Chandini',
AGE = 32 WHERE DEPARTMENT = 'Chemistry';''')
print('\nAfter Updating...\n')

# Display data
print("STAFF Table: ")
data = cursor.execute('''SELECT * FROM STAFF''')
for row in data:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
