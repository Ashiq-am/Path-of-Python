from sqlalchemy.orm import sessionmaker
from Creation import engine, MyTable

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Update the values into the table
session.add(MyTable(data={"first_name": "martha",
						"last_name": "stuart", "age": "45"}))
session.add(MyTable(data={"first_name": "boris",
						"last_name": "johnson", "age": "35"}))
session.add(MyTable(data={"first_name": "vishal",
						"last_name": "kamat", "age": "25"}))
session.commit()

# Query all rows in the table
results = session.query(MyTable).all()
for result in results:
	print(result.id, result.data)

session.commit()
