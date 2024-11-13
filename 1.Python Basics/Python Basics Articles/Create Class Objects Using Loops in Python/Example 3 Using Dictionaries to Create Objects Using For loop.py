class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

product_data = [
	{"name": "Laptop", "price": 1000},
	{"name": "Phone", "price": 800},
	{"name": "Tablet", "price": 500}
]

products = []
for data in product_data:
	product = Product(**data)
	products.append(product)

for product in products:
	print(f"Product: {product.name}, Price: ${product.price}")

person_attributes = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

people = [Person(*attributes) for attributes in person_attributes]

for person in people:
	print(f"Name: {person.name}, Age: {person.age}")
