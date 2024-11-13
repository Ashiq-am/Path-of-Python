from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

# Create an engine and connect to the database
engine = create_engine('sqlite:///mydatabase.db')

# Reflect the existing tables in the database
metadata = MetaData()
metadata.reflect(bind=engine)

# Create a base class for declarative mapping
Base = declarative_base()

# Define the structure of the table using a mapping class
class MyTable(Base):
	__tablename__ = 'my_table'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	value = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Insert some data into the table
engine.execute(MyTable.__table__.insert(), [
	{'name': 'foo', 'value': 1},
	{'name': 'bar', 'value': 2},
	{'name': 'baz', 'value': 3},
])

# Create a session to use for querying
Session = sessionmaker(bind=engine)
session = Session()

# Query the database and get an instance of the mapped class
instance = session.query(MyTable).first()

# Use the inspect function to introspect the instance
inspector = inspect(instance)

# Print the column names
print("Columns:")
for column in inspector.attrs:
	print(f"{column.key}")
