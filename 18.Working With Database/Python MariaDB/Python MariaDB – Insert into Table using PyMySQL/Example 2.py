query = "INSERT INTO PRODUCT (PRODUCT_ID, price,PRODUCT_TYPE) VALUES ('%s', %d, '%s')"

values = [("1203",1000,"ILL"),
		("1523",1500,"broadband"),
		("154",14782,"Voice"),
		]
cur.execute(query,values)
print(f"{cur.rowcount}, details inserted")
conn.commit()
conn.close()
