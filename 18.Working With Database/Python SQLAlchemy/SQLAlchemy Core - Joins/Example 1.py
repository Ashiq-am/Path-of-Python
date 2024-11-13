from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
	__tablename__ = 'customers'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	orders = relationship("Order", back_populates="customer")


class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer, primary_key=True)
	customer_id = Column(Integer, ForeignKey('customers.id'))
	product = Column(String)
	customer = relationship("Customer", back_populates="orders")
