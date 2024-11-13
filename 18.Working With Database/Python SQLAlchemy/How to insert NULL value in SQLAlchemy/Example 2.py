# specify null values as NONE
statement6 = book_publisher.insert().values(
	publisherId=6, publisherName=None, publisherEstd=None)

# insert the null values
engine.execute(statement6)
