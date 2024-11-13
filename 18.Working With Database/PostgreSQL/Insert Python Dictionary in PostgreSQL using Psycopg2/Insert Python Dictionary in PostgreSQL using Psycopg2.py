import psycopg2
import psycopg2

# connection establishment
conn = psycopg2.connect(
    database="geeks",
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE DETAILS(employee_id int NOT NULL,\
		employee_name char(20),
		employee_email varchar(30), employee_salary float);'''

cursor.execute(sql)
dictionary = {'empl1''187643', 'sarah',
              'sarahpaul@gmail.com', '65000'
            'empl2''187644', 'rahul',
              'rahul101@gmail.com', '75000'
        'empl3''187645', 'arjun',
              'arjun234@gmail.com', '70000'
}
columns = dictionary.keys()
for i in dictionary.values():
    sql2 = '''insert into DETAILS(employee_id , employee_name ,
		employee_email , employee_salary) VALUES{};'''.format(i)

cursor.execute(sql2)

sql3 = '''select * from DETAILS;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()
