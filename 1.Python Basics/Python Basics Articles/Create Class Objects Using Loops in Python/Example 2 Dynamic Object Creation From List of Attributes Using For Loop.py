class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

# List of dictionaries containing product attributes
product_data = [
	{"name": "Laptop", "price": 1000},
	{"name": "Phone", "price": 800},
	{"name": "Tablet", "price": 500}
]

# Create Product objects using list comprehension
products = [Product(data["name"], data["price"]) for data in product_data]

# Print the details of each product
for product in products:
	print(f"Product: {product.name}, Price: ${product.price}")
