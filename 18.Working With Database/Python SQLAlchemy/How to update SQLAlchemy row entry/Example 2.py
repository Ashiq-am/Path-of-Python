# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

# update
u = update(BOOKS)
u = u.values({"book_name": "2022 future ahead"})
u = u.where(BOOKS.c.book_id == 3)
engine.execute(u)

# write the SQL query inside the
# text() block to fetch all records
sql = text("SELECT * from BOOKS")

# Fetch all the records
result = engine.execute(sql).fetchall()

# View the records
for record in result:
	print("\n", record)
