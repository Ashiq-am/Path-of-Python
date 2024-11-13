# Get the books table from the Metadata object
BOOKS = meta.tables['books']

# SQLAlchemy Query to select all rows with
# fiction genre
query = sqlalchemy.select(BOOKS).where(BOOKS.c.genre == 'fiction')

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
