from sqlalchemy import create_engine, Table, MetaData, select
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db', echo=True)
Base.metadata.create_all(engine)

# Populate the database with sample data


Session = sessionmaker(bind=engine)
session = Session()

customers = [Customer(name='John'), Customer(name='Jane'),
			Customer(name='Bob'), Customer(name='Mike')]
session.add_all(customers)
session.commit()

orders = [
	Order(product='product_1', customer_id=customers[0].id),
	Order(product='product_2', customer_id=customers[1].id),
	Order(product='product_3', customer_id=customers[0].id),
	Order(product='product_4', customer_id=customers[2].id),
	Order(product='product_5', customer_id=customers[1].id)
]
session.add_all(orders)
session.commit()

# Perform a join query to retrieve data from multiple tables
stmt = select(Order.id, Order.product, Customer.name).select_from(
	Order).join(Customer, Order.customer_id == Customer.id)

results = session.execute(stmt)

for row in results:
	print(row)

session.close()
