# Get the `book_publisher` table from the
# Metadata object
import sqlalchemy

book_publisher = meta.tables['book_publisher']

# SQLAlchemy Query to fetch all records
query = sqlalchemy.select([
	book_publisher])


# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
