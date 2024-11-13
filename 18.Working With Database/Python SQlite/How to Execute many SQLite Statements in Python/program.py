import sqlite3


# make the database connection and cursor object
connection = sqlite3.connect("CollegeData.db")
cursor = connection.cursor()

# create a set of queries in executescript()
# below set of queries will create and insert
# data into table
cursor.executescript("""
	CREATE TABLE department( deptId INTEGER,
	deptName VARCHAR(20), deptScore INTEGER);
	INSERT INTO department VALUES ( 01,'IT', 850 );
	INSERT INTO department VALUES ( 02,'COMP', 840 );
	INSERT INTO department VALUES ( 03,'CIVIL', 500 );
	INSERT INTO department VALUES ( 04,'E&TC', 650 );
""")

# fetch the table data
print("Table data :")
cursor.execute("SELECT * FROM department")
print(cursor.fetchall())

# below set of queries will update the data
# of in the table
cursor.executescript("""
	UPDATE department set deptScore = 900 where deptId = 01;
	UPDATE department set deptScore = 890 where deptId = 02;
	UPDATE department set deptScore = 660 where deptId = 03;
	UPDATE department set deptScore = 790 where deptId = 04;
""")

# fetch the table data after updation
print("Table data after updation :")
cursor.execute("SELECT * FROM department")
print(cursor.fetchall())

# commit the changes and close the database
# connection
connection.commit()
connection.close()
