from sqlalchemy import (create_engine, MetaData, Table,
                        Column, Integer, String, DateTime)

# create a database engine with SQLAlchemy
# and connect to the database server
engine = create_engine('postgresql:'+
					'//demouser:12345678@localhost:5432/demo')

# create a metadata object
metadata = MetaData()

# create a table object for the demo view
demo_view = Table('demo_view', metadata,
				Column('id', Integer, primary_key=True),
				Column('name', String),
				Column('created_at', DateTime)
				)

# create the demo view in the database
metadata.create_all(engine)
