from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, or_, and_, not_

# Create a SQLite engine
engine = create_engine('sqlite:///mydb.database', echo=True)

# Define a metadata object
metadata = MetaData()

# Define a table
students = Table('students', metadata,
				Column('id', Integer, primary_key=True),
				Column('name', String),
				Column('age', Integer),
				Column('gender', String)
				)

# Create the table if it does not exist
metadata.create_all(engine)


# Insert some data into the users table
conn = engine.connect()
conn.execute(students.insert(), [
	{'name': 'Alice', 'age': 25, 'gender': 'Female'},
	{'name': 'John', 'age': 30, 'gender': 'Male'},
	{'name': 'Charlie', 'age': 35, 'gender': 'Male'},
	{'name': 'Jane', 'age': 40, 'gender': 'Male'}
])
