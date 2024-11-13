from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# Define the database connection
engine = create_engine('postgresql://postgres:root@localhost:5432/test')

# Define the session
Session = sessionmaker(bind=engine)
session = Session()

# Define the base model
Base = declarative_base()

# Define the orders table
class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer, primary_key=True)
	customer_id = Column(Integer)
	order_date = Column(String)

# Define the order items table
class OrderItem(Base):
	__tablename__ = 'order_items'
	id = Column(Integer, primary_key=True)
	order_id = Column(Integer, ForeignKey('orders.id'))
	item_name = Column(String)
	item_price = Column(Integer)
	order = relationship(Order, backref='order_items')

# Define the query to join the tables and calculate sums and counts
query = session.query(Order.customer_id,
					func.sum(OrderItem.item_price).label('total_spent'),
					func.count(OrderItem.id).label('item_count')
					).join(OrderItem).group_by(Order.customer_id)

# Execute the query and print the results
for row in query:
	print(f"Customer {row.customer_id}: total spent = {row.total_spent}, item count = {row.item_count}")
