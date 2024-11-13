import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
    database='gfg'
)

# creating cursor object
cursor = conn.cursor()

# creating table
table_st = """CREATE TABLE GEEKS (
           NAME VARCHAR(20) NOT NULL,
           ID INT,
           LANGUAGE VARCHAR(20)
           )"""

# created
cursor.execute(table_st)

# display created tables
cursor.execute("show tables")

# disconnect from server
conn.close()
