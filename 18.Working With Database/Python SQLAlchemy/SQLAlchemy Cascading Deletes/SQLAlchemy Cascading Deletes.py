from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the engine and session
engine = create_engine(
	'mysql+mysqlconnector://root:<your password>@localhost/<your database name>')
Session = sessionmaker(bind=engine)
session = Session()

# Define the models
Base = declarative_base()


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	posts = relationship('Post', backref='user', cascade='all, delete')


class Post(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	body = Column(Text, nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


# Delete a user and all of their posts
user = session.query(User).filter_by(name='John').first()
session.delete(user)
session.commit()

# Check if the user and their posts have been deleted
user = session.query(User).filter_by(name='John').first()
print(user) # This should be None
posts = session.query(Post).filter_by(user_id=1).all()
print(posts) # This should be an empty list
