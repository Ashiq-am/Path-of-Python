from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTIO OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# AUTOMATICALLY MAP THE TABLE MODEL TO USE IT FOR QUERYING
class Payment(Base):

	__table__ = db.Table("payment", Base.metadata, autoload_with=engine)

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=engine)
session = Session()

# PREPARING QUERY USING SQLALCHEMY
result = session.query(
	Payment.customer_id,
	Payment.rental_id,
	Payment.amount,
	Payment.payment_date
).filter(Payment.payment_date > '2005-05-25') \
	.group_by(Payment.customer_id, Payment.rental_id) \
	.all()

# PRINT FIRST 10 RECORDS
for i in range(10):
	r = result[i]
	print(r.customer_id, "|", r.rental_id, "|", r.amount, "|", r.payment_date)
