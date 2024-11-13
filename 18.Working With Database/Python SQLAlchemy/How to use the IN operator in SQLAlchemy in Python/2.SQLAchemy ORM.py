# IMPORT REQUIRED LIBRARIES
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine("mysql+pymysql://\
root:password@localhost/sakila")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Category(Base):

	__tablename__ = 'category'

	category_id = db.Column(
		db.SmallInteger, primary_key=True,
	autoincrement=True)
	name = db.Column(db.String(25))
	last_update = db.Column(db.DateTime)


# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# SELECT category_id, name FROM
# category WHERE name IN
# ("Action", "Horror", "Sci-Fi");
result = session.query(Category.category_id, Category.name) \
	.filter(
		Category.name.in_(("Action", "Horror", "Sci-Fi"))
)

# VIEW THE ENTRIES IN THE RESULT
for record in result:
	print("\n", record.category_id, "-", record.name)
