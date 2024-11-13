from sqlalchemy.orm import sessionmaker
from Creation import engine, MyTable

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Update the values into the table
# Delete a row based on id
session.query(MyTable).filter(MyTable.id == 2).delete()
session.commit()


# Query all rows in the table
results = session.query(MyTable).all()
for result in results:
	print(result.id, result.data)

session.commit()
# closes the session here
session.close()
