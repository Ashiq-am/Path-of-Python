# import the mysql client for python

import pymysql

# Create a connection object
# IP address of the MySQL database server
Host = "localhost"
# User name of the database server
User = "user"
# Password for the database user
Password = ""

database = "database_name"

conn = pymysql.connect(host=Host, user=User, password=Password, database=database)

# Create a cursor object
cur = conn.cursor()

PRODUCT_ID = '1201'
price = 10000
PRODUCT_TYPE = 'PRI'

query = f"INSERT INTO PRODUCT (PRODUCT_ID, price,PRODUCT_TYPE) VALUES ('{PRODUCT_ID}', '{price}', '{PRODUCT_TYPE}')"

cur.execute(query)
print(f"{cur.rowcount} details inserted")
conn.commit()
conn.close()
