# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

# SQLAlchemy Query to GROUP BY and filter function
query = sqlalchemy.select([
	BOOKS.c.genre,
	sqlalchemy.func.count(BOOKS.c.genre)
]).group_by(BOOKS.c.genre).filter(BOOKS.c.book_price > 50.0)

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
