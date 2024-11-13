from sqlalchemy import create_engine, Column, Boolean, Float, Decimal, LargeBinary

engine = create_engine('sqlite:///example.db')
metadata = Base.metadata

product_table = Table('products', metadata,
	Column('id', Integer, primary_key=True),
	Column('completed', Boolean),
	Column('price', Float),
	Column('discount', Decimal(10, 2)),
	Column('image', LargeBinary),
)

metadata.create_all(engine)
