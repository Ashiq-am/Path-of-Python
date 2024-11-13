from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine(
	"mysql+pymysql://root:password@localhost/Geeks4Geeks")

# CREATE THE SALES TABLE MODEL
# TO USE IT FOR QUERYING
class Sales(Base):

	__tablename__ = 'sales'

	product = db.Column(db.String(50),
						primary_key=True)
	quantity = db.Column(db.Integer)
	description = db.Column(db.String(100),
							default=None)


# CREATE SALES TABLE IF IT
# DOES NOT EXIST ALREADY
Base.metadata.create_all(engine,
						tables=[Sales.__table__])

# CREATE A SESSION OBJECT TO
# COMMIT SQL QUERIES TO DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# INSERT NEW RECORD WITH A DESCRIPTION
new_record = Sales(product='Refrigerator',
				quantity=15,
				description='The season is too hot!')
session.add(new_record)
session.commit()

# INSERT NEW RECORD WITHOUT DESCRIPTION SO
# THAT IT TAKES DEFAULT NULL VALUE AS DEFINED
new_record = Sales(product='Washing Machine',
				quantity=12)
session.add(new_record)
session.commit()
