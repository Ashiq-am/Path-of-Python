# Import necessary modules
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the Database Tables
class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String(20))
	email = Column(String(20))
	profile = relationship("Profile", uselist=False, back_populates="user")


class Profile(Base):
	__tablename__ = 'profiles'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'), unique=True)
	bio = Column(String(20))
	user = relationship("User", back_populates="profile")


# Create the Database Connection
engine = create_engine('your_database_url')

# Create the table
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Perform Bulk Insert
users = [
	User(name='John', email='john@example.com'),
	User(name='Alice', email='alice@example.com')
]

profiles = [
	Profile(bio='Bio for John', user=users[0]),
	Profile(bio='Bio for Alice', user=users[1])
]

session.add_all(users)
session.add_all(profiles)
session.commit()

# Verify the Results
users = session.query(User).all()
profiles = session.query(Profile).all()

print("Inserted Users:")
for user in users:
	print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

print("Inserted Profiles:")
for profile in profiles:
	print(f"ID: {profile.id}, User ID: {profile.user_id}, Bio: {profile.bio}")

# Close the Session
session.close()
