from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker

# create an in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
users_table = Table('users', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String),
	Column('fullname', String),
	Column('password', String)
)

class User:
	def __init__(self, name, fullname, password):
		self.name = name
		self.fullname = fullname
		self.password = password

	def __repr__(self):
		return f"<User(name='{self.name}', fullname='{self.fullname}', password='{self.password}')>"

# create a mapper to map the User class to the users table
mapper(User, users_table)

# create the users table
metadata.create_all(engine)

# create a session to manage the connection to the database
Session = sessionmaker(bind=engine)
session = Session()

# add a new user to the database
user = User(name='john', fullname='John Doe', password='password')
session.add(user)
session.commit()

# query the users table
users = session.query(User).all()
print(users)
# Output: [<User(name='john', fullname='John Doe', password='password')>]
