class Product:
    def __init__(self, price):
        self.price = price

product = Product(100)
product.price = -50  # This is not ideal, as negative prices don't make sense.
print(product.price)  # Output: -50
