# Get the `books` table from the
# Metadata object
BOOKS = meta.tables['books']

# Write a SQL query using groupby
# and count function
query = sqlalchemy.select([
	BOOKS.c.genre,
	sqlalchemy.func.count(BOOKS.c.genre)
]).group_by(BOOKS.c.genre)

# get all the records
result = engine.execute(query).fetchall()

# print all the records
for i in result:
	print("\n", i)
