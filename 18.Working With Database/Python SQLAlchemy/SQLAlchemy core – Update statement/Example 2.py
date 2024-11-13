# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

# update
stmt = BOOKS.update().where(BOOKS.c.genre == 'non-fiction'
						).values(genre = 'sci-fi')
engine.execute(stmt)

# write the SQL query inside the
# text() block to fetch all records
sql = text("SELECT * from BOOKS")

# Fetch all the records
result = engine.execute(sql).fetchall()

# View the records
for record in result:
	print("\n", record)
