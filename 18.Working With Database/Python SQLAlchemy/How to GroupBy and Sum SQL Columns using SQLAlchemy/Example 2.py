import sqlalchemy as db

# Define the Engine (Connection Object)
engine = db.create_engine(
	"mysql+pymysql://root:password@localhost/Geeks4Geeks")

# Create the Metadata Object
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# Get the `students` table from the Metadata object
STUDENTS = meta_data.tables['students']

# SQLAlchemy Query to GROUP BY and aggregate SUM
query = db.select([
	STUDENTS.c.first_name,
	STUDENTS.c.last_name,
	db.func.sum(STUDENTS.c.score)
]).group_by(STUDENTS.c.first_name, STUDENTS.c.last_name)

# Fetch all the records
result = engine.execute(query).fetchall()

# View the records
for record in result:
	print("\n", record[0], record[1],
		"| Total Score:", record[2])
