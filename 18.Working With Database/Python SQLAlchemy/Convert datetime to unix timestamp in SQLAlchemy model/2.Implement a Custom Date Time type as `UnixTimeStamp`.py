# define a custom type for unix timestamp
class UnixTimestamp(TypeDecorator):

	# convert unix timestamp to datetime object
	impl = Integer

	# convert datetime object to unix timestamp when inserting data to database
	def process_bind_param(self, value, dialect):
		if value is not None:
			return int(value.timestamp())
		else:
			return None
