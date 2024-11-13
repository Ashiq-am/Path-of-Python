from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///example.db')

# Create a SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()

# Define a SQLAlchemy model
Base = declarative_base()


class Example(Base):
	__tablename__ = 'example'
	id = Column(Integer, primary_key=True)
	value = Column(Integer)


# Create the example table
Base.metadata.create_all(engine)

# Insert some data into the example table
session.add(Example(value=1))
session.add(Example(value=2))
session.add(Example(value=3))
session.commit()

# Use a mathematical equation as a filter in a query
results = session.query(Example).filter(Example.value * 2 > 3).all()

# Print the results
for result in results:
	print(result.value)

# Output: 2, 3
