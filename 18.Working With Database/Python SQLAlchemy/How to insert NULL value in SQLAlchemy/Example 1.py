# import necessary packages
from sqlalchemy import create_engine,MetaData, Table, Column, Integer, String

# establish connection
engine = create_engine(
	"database+dialect://username:password@hostname:port/database_name")

# store engine objects
meta = MetaData()

# create a table
book_publisher = Table(
	'book_publisher', meta,
	Column('publisherId', Integer, primary_key=True),
	Column('publisherName', String),
	Column('publisherEstd', Integer),
)

# use create_all() function to create a
# table using objects stored in meta.
meta.create_all(engine)

# insert values
statement1 = book_publisher.insert().values(
	publisherId=1, publisherName="Oxford", publisherEstd=1900)
statement2 = book_publisher.insert().values(
	publisherId=2, publisherName='Stanford', publisherEstd=1910)
statement3 = book_publisher.insert().values(
	publisherId=3, publisherName="MIT", publisherEstd=1920)
statement4 = book_publisher.insert().values(
	publisherId=4, publisherName="Springer", publisherEstd=1930)
statement5 = book_publisher.insert().values(
	publisherId=5, publisherName="Packt", publisherEstd=1940)

engine.execute(statement1)
engine.execute(statement2)
engine.execute(statement3)
engine.execute(statement4)
engine.execute(statement5)
