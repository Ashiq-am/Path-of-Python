# IMPORT THE REQUIRED LIBRARY
import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://\
root:password@localhost/sakila")

# CREATE THE METADATA OBJECT TO ACCESS THE TABLE
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# GET THE `payment` TABLE FROM THE METADATA OBJECT
payment_table = meta_data.tables['payment']

# SELECT MAX(amount) FROM sakila.`payment`;
query = db.select([db.func.max(payment_table.c.amount)])

# FETCH ALL THE RECORDS IN THE RESPONSE
result = engine.execute(query).first()

# VIEW THE RESULT
print(result[0])
