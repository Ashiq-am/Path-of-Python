# import necessary packages
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, String, Column, Numeric, Integer, VARCHAR, \
    update, text, delete
from sqlalchemy.engine import result

# establish connection
engine = create_engine(
	"database+dialect://username:password@hostname:port/databasename")

# store engine objects
meta = MetaData()

# create a table
book_publisher = Table(
	'book_publisher', meta,
	Column('publisher_id', Integer,
		primary_key=True),
	Column('publisher_name', String),
	Column('publisher_estd', Integer),
)

# use create_all() function to create
# a table using objects stored in meta.
meta.create_all(engine)

# insert values
statement1 = book_publisher.insert().values(
	publisher_id=1, publisher_name="Oxford",
publisher_estd=1900)
statement2 = book_publisher.insert().values(
	publisher_id=2, publisher_name='Stanford',
publisher_estd=1910)
statement3 = book_publisher.insert().values(
	publisher_id=3, publisher_name="MIT",
publisher_estd=1920)
statement4 = book_publisher.insert().values(
	publisher_id=4, publisher_name="Springer",
publisher_estd=1930)
statement5 = book_publisher.insert().values(
	publisher_id=5, publisher_name="Packt",
publisher_estd=1940)

engine.execute(statement1)
engine.execute(statement2)
engine.execute(statement3)
engine.execute(statement4)
engine.execute(statement5)

# Get the `book_publisher` table from the Metadata object
book_publisher = meta.tables['book_publisher']
