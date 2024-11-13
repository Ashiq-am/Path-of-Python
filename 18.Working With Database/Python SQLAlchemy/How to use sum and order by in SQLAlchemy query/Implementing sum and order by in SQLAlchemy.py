# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

# SQLAlchemy Query to use sum and order by function
query = sqlalchemy.select([
	BOOKS.c.genre,
	sqlalchemy.func.sum(BOOKS.c.book_price)
]).group_by(BOOKS.c.genre).order_by(BOOKS.c.genre)

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
