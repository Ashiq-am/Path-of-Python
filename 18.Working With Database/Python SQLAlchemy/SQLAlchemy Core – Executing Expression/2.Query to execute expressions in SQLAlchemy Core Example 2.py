# write the SQL query inside the text() block
sql = text("SELECT * from BOOKS WHERE BOOKS.book_price/10 =10")

# Fetch all the records
result = engine.execute(sql).fetchall()

# View the records
for record in result:
	print("\n", record)
