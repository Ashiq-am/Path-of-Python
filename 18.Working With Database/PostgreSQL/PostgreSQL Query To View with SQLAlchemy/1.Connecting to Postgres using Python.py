from sqlalchemy import create_engine

# create a database engine with SQLAlchemy and connect to the database server
# url format: dialect+driver://username:password@host:port/database
engine = create_engine('postgresql://demouser:12345678@localhost:5432/demo')

# connect to the database and printing connection successful if connected
with engine.connect() as conn:
	print("Connection successful")
