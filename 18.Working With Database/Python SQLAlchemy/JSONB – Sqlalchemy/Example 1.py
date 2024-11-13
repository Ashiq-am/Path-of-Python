from sqlalchemy import create_engine, Table, Column, Integer, MetaData, JSON
from sqlalchemy.dialects.postgresql import JSONB, insert

engine = create_engine('postgresql://vikadmin:dbpass@localhost:5432/vikashdb')
metadata = MetaData()


# reflect the database schema to the metadata
metadata.reflect(bind=engine)

users = Table('users', metadata,
	Column('id', Integer, primary_key=True),
	Column('data', JSONB),
	extend_existing=True
)

metadata.create_all(engine)


# get the table object
table_name = 'users'
table = metadata.tables[table_name]

# print the table schema
print(table.__repr__())
