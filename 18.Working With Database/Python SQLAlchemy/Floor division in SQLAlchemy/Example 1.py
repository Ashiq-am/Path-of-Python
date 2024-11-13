# import necessary packages
from sqlalchemy import (create_engine, MetaData,
Table, Column, Numeric, Integer)

# establish connections
engine = create_engine(
	"postgresql+psycopg2://postgres:Saibaba97%40@127.0.0.1:5432/test")

# initialize meta data
meta = MetaData()

# create a table schema
books = Table(
	'books', meta,
	Column('bookId', Integer, primary_key=True),
	Column('book_price', Numeric),
)

meta.create_all(engine)

# insert records into the table
statement1 = books.insert().values(bookId=1,
								book_price=12.2)
statement2 = books.insert().values(bookId=2,
								book_price=13.2)
statement3 = books.insert().values(bookId=3,
								book_price=121.6)
statement4 = books.insert().values(bookId=4,
								book_price=100)
statement5 = books.insert().values(bookId=5,
								book_price=1112.2)

# execute the insert records statement
engine.execute(statement1)
engine.execute(statement2)
engine.execute(statement3)
engine.execute(statement4)
engine.execute(statement5)
