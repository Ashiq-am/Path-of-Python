# write a conventional SQL query
# with NULL equivalent as None
s = book_publisher.select().where(
book_publisher.c.publisherName == None)

# output get stored in result object
result = engine.execute(s)

# iteratte through the result object
# to get all rows of the output
for row in result:
	print(row)
