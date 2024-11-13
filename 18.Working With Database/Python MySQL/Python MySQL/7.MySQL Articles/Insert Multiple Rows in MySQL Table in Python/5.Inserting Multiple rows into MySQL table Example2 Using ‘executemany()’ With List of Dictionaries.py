import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
    database='gfg'
)

# creating cursor object
cursor = conn.cursor()

insert_st = "INSERT INTO GEEKS(NAME, ID, LANGUAGE)
VALUES ( % (NAME)s, % (ID)s, % (LANGUAGE)s)"
values = [
    {'NAME': 'geek5', 'ID': '3678', 'LANGUAGE': 'Eng'},
    {'NAME': 'geek6', 'ID': '7896', 'LANGUAGE': 'punjabi'},
    {'NAME': 'geek7', 'ID': '4016', 'LANGUAGE': 'Hindi'}
]

# executemany() method
cursor.executemany(insert_st, values)

# save changes
conn.commit()

# disconnect from sever
conn.close()
