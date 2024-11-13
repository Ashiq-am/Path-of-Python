import sqlalchemy as db

# Define the Engine (Connection Object)
engine = db.create_engine("sqlite:///users.db")

# Create the Metadata Object
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# Get the `employees` table from the Metadata object
EMPLOYEES = meta_data.tables['employees']

# SQLAlchemy Query to extract DISTINCT records
query = db.select([db.distinct(EMPLOYEES.c.emp_address)])

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record)
