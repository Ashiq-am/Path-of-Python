from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the Base object
Base = declarative_base()

# Define your model class
class BlogPost(Base):
	__tablename__ = 'blog_posts'

	id = Column(Integer, primary_key=True)
	title = Column(String)
	content = Column(String)

	# Add any other columns or relationships here

# Replace 'sqlite:///example.db' with your desired database connection string
DATABASE_URL = 'sqlite:///example.db'

try:
	engine = create_engine(DATABASE_URL)
	Base.metadata.create_all(bind=engine)

	Session = sessionmaker(bind=engine)
	session = Session()

	# Your code using the session goes here

except Exception as e:
	print(f"An error occurred: {e}")

finally:
	# Ensure that the session is closed, regardless of success or failure
	if session:
		session.close()
