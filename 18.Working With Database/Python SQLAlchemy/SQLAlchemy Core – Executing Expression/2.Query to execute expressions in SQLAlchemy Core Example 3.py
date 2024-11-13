# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']


from sqlalchemy import insert
# write the insert statement
stmt1 = insert(BOOKS).values(book_id=6,
							book_price=400,
							genre="fiction",
							book_name="yoga is science")
stmt2 = insert(BOOKS).values(book_id=7,
							book_price=800,
							genre="non-fiction",
							book_name="alchemy tutorials")
# execute
engine.execute(stmt1)
engine.execute(stmt2)

# write the SQL query to check
# whether the records are inserted
sql = text("SELECT * FROM BOOKS ")

results = engine.execute(sql)

# View the records
for record in results:
	print("\n", record)
