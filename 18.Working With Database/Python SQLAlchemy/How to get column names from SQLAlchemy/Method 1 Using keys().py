import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine(
	"mysql+pymysql://root:password@localhost/Geeks4Geeks")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Profile(Base):

	__tablename__ = 'profile'

	email = db.Column(db.String(50), primary_key=True)
	name = db.Column(db.String(100))
	contact = db.Column(db.Integer)


# PREPARING SQLALCHEMY QUERY
with engine.connect() as conn:
	result = conn.execute(
		db.select([Profile.email, Profile.name,
				Profile.contact]))

# VIEW THE COLUMN NAMES
print(result.keys())
