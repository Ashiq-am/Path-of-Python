import sqlalchemy as db

# Define the Engine (Connection Object)
engine = db.create_engine(
	"mysql+pymysql://root:password@localhost/Geeks4Geeks")

# Create the Metadata Object
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# Get the `sales` table from the Metadata object
SALES = meta_data.tables['sales']

# SQLAlchemy Query to GROUP BY and aggregate SUM
query = db.select([SALES.c.company, db.func.sum(SALES.c.no_of_invoices)]) \
	.group_by(SALES.c.company)

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", "Company:", record[0],
		"| Sum of Invoices:",
		record[1])
