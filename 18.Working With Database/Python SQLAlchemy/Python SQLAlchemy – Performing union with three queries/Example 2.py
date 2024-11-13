from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Payment(Base):

	__table__ = db.Table("payment", Base.metadata, autoload_with=engine)

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# PREPARING QUERY USING SQLALCHEMY
query_1 = session.query(Payment).filter(Payment.payment_id == 1)
query_2 = session.query(Payment).filter(Payment.payment_id == 2)
query_3 = session.query(Payment).filter(Payment.payment_id == 3)

# EXTRACT ALL THE RECORDS BY PERFORMING UNION OF THREE QUERIES
result = query_1.union(query_2, query_3).all()

# PRINT THE RESULTANT RECORDS
for r in result:
	print(r.payment_id, "|", r.customer_id, "|", r.rental_id, "|", r.amount)
