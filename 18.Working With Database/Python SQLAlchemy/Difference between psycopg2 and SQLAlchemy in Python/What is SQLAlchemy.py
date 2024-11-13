from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database engine
engine = create_engine('postgresql://username:password@localhost/mydatabase')

# Base class for the ORM models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create the database table
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user to the database
new_user = User(name='John Doe', email='john.doe@example.com')
session.add(new_user)
session.commit()

# Query the user
user = session.query(User).filter_by(name='John Doe').first()
print(user.email)
