import sqlalchemy as db

# Define the Engine (Connection Object)
engine = db.create_engine(
	"mysql+pymysql://root:password@localhost/Geeks4Geeks")

# Create the Metadata Object
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# Get the `students` table from the Metadata object
STUDENTS = meta_data.tables['students']

# SQLAlchemy Query to get AVG
query = db.select([db.func.round(db.func.avg(STUDENTS.c.percentage), 2)])

# Fetch the records
avg_result = engine.execute(query).fetchall()

# SQLAlchemy Query to get SUM
query = db.select([db.func.round(db.func.sum(STUDENTS.c.percentage), 2)])

# Fetch the records
sum_result = engine.execute(query).fetchall()

# View the records
print("\nAverage: ", avg_result[0])
print("\nSum: ", sum_result[0])
