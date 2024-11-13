from sqlalchemy import delete

# query to multiple table delete
delete_stmt = (delete(BOOKS).where(
BOOKS.c.book_id == book_publisher.c.publisher_id).where(
	book_publisher.c.publisher_name == 'Springer'))

# execute the statement
engine.execute(delete_stmt)

# write the SQL query inside the
# text() block to fetch all records
sql = text("SELECT * from BOOKS")

# Fetch all the records
result = engine.execute(sql).fetchall()

# View the records
for record in result:
	print("\n", record)
