# code
from sqlalchemy import create_engine, Table, Column, Integer, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import text
from sqlalchemy import MetaData

engine = create_engine('postgresql://vikadmin:dbpass@localhost:5432/vikashdb')
metadata = MetaData()

# Defining the Table schema, using extend_existing
# will allow to rerun the code
# when table already exist in the database.
employeest = Table('employeest', metadata,
				Column('id', Integer,
						primary_key=True),
				Column('info', JSONB),
				extend_existing=True)
metadata.create_all(engine)
