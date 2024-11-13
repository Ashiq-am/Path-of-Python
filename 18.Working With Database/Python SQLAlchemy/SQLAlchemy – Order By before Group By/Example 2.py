# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

# SQLAlchemy Query to ORDER BY and GROUP BY
query = sqlalchemy.select([
	BOOKS.c.genre, sqlalchemy.func.sum(BOOKS.c.book_price)
]).order_by(BOOKS.c.genre).group_by(BOOKS.c.genre)

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
