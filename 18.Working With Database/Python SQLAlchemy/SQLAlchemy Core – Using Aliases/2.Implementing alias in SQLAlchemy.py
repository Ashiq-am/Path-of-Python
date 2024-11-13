# Get the `books` table from the Metadata object
from sqlalchemy.sql import alias, select
BOOKS = meta.tables['books']

b = BOOKS.alias("a")
s = select([b]).where(b.c.book_id > 2)

# Fetch all the records
result = engine.execute(s).fetchall()

# View the records
for record in result:
	print("\n", record)
