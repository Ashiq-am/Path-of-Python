products = session.query(product_table).filter(product_table.c.price < 10).all()

for product in products:
	print(product)
