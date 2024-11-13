from sqlalchemy.orm import sessionmaker
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


class Location(Base):

	__tablename__ = 'location'

	email = db.Column(db.String(50), primary_key=True)
	location = db.Column(db.String(100))


# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# SELECT * FROM PROFILE
result = session.query(
	Profile.email,
	Profile.name,
	Profile.contact,
	Location.location
).join(Location, Profile.email == Location.email)

print("Query:", result)
print()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
	print(r.email, "|", r.name, "|", r.contact, "|", r.location)
