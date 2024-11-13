from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# commiting a user to database with created_at in unix timestamp
user = User(name='John')

# create an engine
engine = create_engine('sqlite:///unix_timestamp.db', echo=True)

# create the table
Base.metadata.create_all(engine)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# add the user to the session
session.add(user)

# commit the session
session.commit()
