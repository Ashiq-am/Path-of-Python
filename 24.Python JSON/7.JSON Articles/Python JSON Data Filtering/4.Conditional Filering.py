import json

# Sample JSON array of products
products_data = '[{"name": "Laptop", "price": 1200, "stock": 5}, {"name": "Headphones", "price": 80, "stock": 0}, {"name": "Mouse", "price": 20, "stock": 10}]'
products = json.loads(products_data)

# Conditional filtering
in_stock_products = [product for product in products if product["stock"] > 5]
print(in_stock_products)
