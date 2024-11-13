from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_product = product_table.insert().values(completed=True, price=9.99, discount=1.50, image=b'\x00\x01\x02')
session.execute(new_product)
session.commit()
