import pymysql

conn = pymysql.connect('localhost','user','password','GFG')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS PRODUCT")
query = """CREATE TABLE PRODUCT (
		PRODUCT_ID CHAR(20) NOT NULL,
		price int(10),
		PRODUCT_TYPE VARCHAR(64) ) """

# To execute the SQL query
cur.execute(query)

# To commit the changes
conn.commit()
conn.close()
