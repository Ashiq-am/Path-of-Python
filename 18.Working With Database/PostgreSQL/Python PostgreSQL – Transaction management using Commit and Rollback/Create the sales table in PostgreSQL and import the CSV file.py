# import packages
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# establish connections
conn_string = 'postgres://postgres:pass@127.0.0.1/SuperMart'

db = create_engine(conn_string)
conn = db.connect()
conn1 = psycopg2.connect(
database="SuperMart", user='postgres',
password='pass', host='127.0.0.1', port='5432'
)

conn1.autocommit = True
cursor = conn1.cursor()

# drop table if it already exists
cursor.execute('drop table if exists sales')

sql = '''CREATE TABLE sales(Order_Line int,\
Order_ID char(20),Order_Date Date,Ship_Date Date,\
Ship_Mode char(20) ,Customer_ID char(20),Product_ID char(20),\
Sales decimal,Quantity int,Discount decimal,Profit decimal);'''

cursor.execute(sql)

# import the csv file to create a dataframe
data = pd.read_csv("Sales.csv")

# converting data to sql
data.to_sql('sales', conn, if_exists='replace')

# fetching all rows
sql1 = '''select * from sales;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

conn1.commit()
conn1.close()
