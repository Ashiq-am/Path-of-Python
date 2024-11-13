from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///example.db')
metadata = MetaData()

# Define a table with column and data types
users = Table(
	'users', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String),
	Column('age', Integer),
)

# Create the table in the database
metadata.create_all(engine)

# Insert some data into the table
conn = engine.connect()
conn.execute(users.insert().values(name='Alice', age=25))
conn.execute(users.insert().values(name='Bob', age=30))

# Select all users from the table
result = conn.execute(users.select())

# Print the results
for row in result:
	print(row)
