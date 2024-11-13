from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData

engine = create_engine('sqlite:///example.db')
metadata = MetaData()

# Define a table with column and data types
articles = Table(
	'articles', metadata,
	Column('id', Integer, primary_key=True),
	Column('title', String),
	Column('content', String),
	Column('published_at', DateTime),
)

# Create the table in the database
metadata.create_all(engine)

# Insert some data into the table
conn = engine.connect()
conn.execute(articles.insert().values(
	title='Intro to SQLAlchemy',
	content='In this article, we will learn how to use SQLAlchemy to interact with databases.',
	published_at='2022-02-28 12:00:00'
))

# Select all articles from the table
result = conn.execute(articles.select())

# Print the results
for row in result:
	print(row)
