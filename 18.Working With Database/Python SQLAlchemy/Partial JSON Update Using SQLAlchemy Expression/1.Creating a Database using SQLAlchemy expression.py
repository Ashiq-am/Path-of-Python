# Importing required modules
from sqlalchemy import Column, String, Integer,\
	create_engine, JSON
from sqlalchemy.orm import declarative_base,\
	sessionmaker
from sqlalchemy import update, func
import os

# Defining the path of database.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///"+os.path.join(BASE_DIR,
											'site.db')

# Create a base class
Base = declarative_base()

# Create a new database engine instance
engine = create_engine(connection_string,
					echo=True)

# Creates a session for objects
Session = sessionmaker()
local_session = Session(bind=engine)

# Defining the schema of the table
class User(Base):
	__tablename__ = 'users'
	id = Column(Integer(),
				primary_key=True)
	username = Column(String(25),
					nullable=False,
					unique=True)
	info = Column(JSON,
				nullable=True)

	def __repr__(self):
		return f"<User username={self.username}>"


Base.metadata.create_all(engine)
