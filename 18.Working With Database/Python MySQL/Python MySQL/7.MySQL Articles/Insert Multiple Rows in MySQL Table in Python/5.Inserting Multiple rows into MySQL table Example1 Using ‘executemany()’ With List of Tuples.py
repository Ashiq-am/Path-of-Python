import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
    database='gfg'
)

# creating cursor object
cursor = conn.cursor()

insert_st = "INSERT INTO GEEKS (NAME, ID, LANGUAGE) VALUES (%s, %s, %s)"
values = [
    ('geek2', '1123', 'Hindi'),
    ('geek3', '3124', 'Telugu'),
    ('geek4', '4567', 'Urdu')
]

# executemany() method
cursor.executemany(insert_st, values)

# save changes
conn.commit()

# disconnect from server
conn.close()
