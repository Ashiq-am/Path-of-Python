import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
    database='gfg'
)

# creating cursor object
cursor = conn.cursor()

insert_st = "INSERT INTO GEEKS(NAME, ID, LANGUAGE) VALUES"
values = [
    ('geek8', '3604', 'Telugu'),
    ('geek9', '2495', 'Hindi'),
    ('geek10', '7895', 'Tamil')
]

# constructing sql statment with multiple row values
for row in values:
    insert_st += "('{}','{}','{}'),".format(row[0], row[1], row[2])

insert_st = insert_st[:-1]

# create rows
cursor.execute(insert_st)

# save changes
conn.commit()

# disconnect from server
conn.close()
