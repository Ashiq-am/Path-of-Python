import pymysql

# Create a connection object
conn = pymysql.connect('localhost', 'user',
						'password', 'database')

# Create a cursor object
cur = conn.cursor()


query = f"update PRODUCT set PRODUCT_ID = 'A123' WHERE \
price = 14782 AND PRODUCT_TYPE = 'Voice'"

cur.execute(query)

# To commit the changes
conn.commit()
conn.close()
