# create a base class for the models
Base = declarative_base()

# create a model for the user
class User(Base):
	__tablename__ = 'users'

	# define the columns of the user table
	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	# using the custom defined type for created_at column
	created_at = Column(UnixTimestamp, default=datetime.datetime.utcnow())

	# used while printing the user object from the database
	def __repr__(self):
		return f"User(id={self.id}, name={self.name}, created_at={self.created_at})"
