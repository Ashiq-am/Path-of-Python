import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
    database='gfg'
)

# creating cursor object
cursor = conn.cursor()

# insert command/statement
insert_st = """INSERT INTO GEEKS(NAME,ID,LANGUAGE) 
             VALUES("geek1","1234","eng")"""

# row created
cursor.execute(insert_st)
# save changes
conn.commit()

# disconnect from server
conn.close()
