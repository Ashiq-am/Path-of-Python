import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@localhost/sakila")

# CREATE THE METADATA OBJECT TO ACCESS THE TABLE
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# GET THE `payment` TABLE FROM THE METADATA OBJECT
payment = meta_data.tables['payment']

# PREPARING QUERY
query = db.select(
	payment.c.customer_id,
	payment.c.rental_id,
	payment.c.amount,
	payment.c.payment_date
).filter(payment.c.payment_date > '2005-05-25') \
	.group_by(payment.c.customer_id, payment.c.rental_id)

# EXTRACT THE RECORDS USING THE QUERY AND ENGINE
with engine.connect() as conn:
	result = conn.execute(query).all()

# PRINT FIRST 10 RECORDS
for i in range(10):
	r = result[i]
	print(r.customer_id, "|", r.rental_id, "|", r.amount, "|", r.payment_date)
