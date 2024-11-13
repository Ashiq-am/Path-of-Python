from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connects to database engine used mysql
engine = create_engine('mysql://roots:PASSWORD@localhost:3306/trial')
Base = declarative_base()

# Creating a table in database with two colums id and data
# for this example the entire json file is stored in data
class MyTable(Base):
	__tablename__ = 'employees'
	id = Column(Integer, primary_key=True)
	data = Column(JSON)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert a row with a JSON column
session.add(MyTable(data={"first_name": "joseph",
						"last_name": "matthew", "age": "18"}))
session.commit()

# Query the table using the JSON column
result = (
	session.query(MyTable)
	.filter(MyTable .data["first_name"] == "joseph")
	.all()
)

for result in result:

	print(result.id) # prints 1
