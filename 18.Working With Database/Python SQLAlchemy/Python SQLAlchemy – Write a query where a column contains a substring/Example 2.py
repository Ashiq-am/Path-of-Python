# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

# SQLAlchemy Query to pick
# records containing substring fiction
query = sqlalchemy.select([
	BOOKS.c.book_name,
]).filter(BOOKS.c.genre.contains("fiction"))


# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
