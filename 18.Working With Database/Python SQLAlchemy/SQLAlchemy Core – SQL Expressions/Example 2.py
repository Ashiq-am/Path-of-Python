# define a tuple of dictionary of values to be inserted
data = ( { "book_id": 6, "book_price": 400,
		"genre": "fiction",
		"book_name": "yoga is science" },
		{ "book_id": 7, "book_price": 800,
		"genre": "non-fiction",
		"book_name": "alchemy tutorials" },
)

# write the insert statement
statement = text("""INSERT INTO BOOKS\
(book_id, book_price, genre, book_name) \
VALUES(:book_id, :book_price, :genre, :book_name)""")

# insert the data one after other using
# execute statement by unpacking dictionary elements
for line in data:
	engine.execute(statement, **line)

# write the SQL query to check
# whether the records are inserted
sql = text("SELECT * FROM BOOKS ")

results = engine.execute(sql)

# View the records
for record in results:
	print("\n", record)
