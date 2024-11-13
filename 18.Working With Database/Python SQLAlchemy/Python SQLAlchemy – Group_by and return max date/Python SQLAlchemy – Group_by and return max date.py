import sqlalchemy as db
from sqlalchemy.engine import result

# Define the Engine (Connection Object)
engine = db.create_engine("mysql+pymysql://root:password@localhost/Geeks4Geeks")

# Create the Metadata Object
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# Get the `users` table from the Metadata object
USERS = meta_data.tables['users']

# SQLAlchemy Query to GROUP BY and fetch MAX date
query = db.select([
	USERS.c.email,
	USERS.c.first_name,
	USERS.c.last_name,
	db.func.max(USERS.c.created_on)
]).group_by(USERS.c.first_name, USERS.c.last_name)

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
