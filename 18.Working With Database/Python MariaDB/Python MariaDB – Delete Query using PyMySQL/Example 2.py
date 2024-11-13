import pymysql

# Create a connection object
conn = pymysql.connect('localhost', 'user',
						'password', 'database')

# Create a cursor object
cur = conn.cursor()


query = f"DELETE FROM PRODUCT WHERE price < 2000"

cur.execute(query)

# To commit the changes
conn.commit()
conn.close()
