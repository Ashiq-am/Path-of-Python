# import packages
import psycopg2
import pandas as pd
from sqlalchemy import create_engine


# creating a connection
conn_string = 'postgres://postgres:sherlockedisi@127.0.0.1/data1'

db = create_engine(conn_string)
conn = db.connect()

#creating a table
sql = '''CREATE TABLE details(Name char(20),
		Age int);'''


# initialise data of lists.
data = {'Name':['sam', 'richie', 'harry'],
		'Age':[18, 20, 19]}

# Create DataFrame
df = pd.DataFrame(data)
df.to_sql('data', con=conn, if_exists='replace', index=False)
conn = psycopg2.connect(conn_string
						)
conn.autocommit = True
cursor = conn.cursor()

# fetching data
sql1='''select * from data;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

# conn.commit()
conn.close()
