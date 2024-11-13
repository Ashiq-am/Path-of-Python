from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declare Mapping
Base = declarative_base()


# This is the class which is mapped to "posts"
# table to our database
class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True, nullable=False)
	title = Column(String, nullable=False)
	content = Column(String, nullable=False)
	published = Column(Boolean, server_default='true', nullable=False)


# Syntax of database url = "<database_vendor_name>://
# <username>:<password>@ip-address/hostname/<database_name>"
DB_URL = "postgresql://anurag:anurag@localhost/gfg"

engine = create_engine(DB_URL)

local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# With this we get a session to do whatever we
# want to do
db = local_session()

# New post created by a user, assumes you get this
# from the frontend
post = Post(title="GFG Article",
			content="How to add SQL Alchemy objects", published=True)

db.add(post)
db.commit()

# After performing transaction, we should always close
# our connection to the database
db.close()

print("Successfully added a new post")
