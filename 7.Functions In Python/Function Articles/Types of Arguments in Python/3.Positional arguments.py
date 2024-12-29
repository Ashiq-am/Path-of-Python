def productInfo(product, price):
    print("Product:", product)
    print("Price: $", price)


# Correct order of arguments
print("Case-1:")
productInfo("Laptop", 1200)

# Incorrect order of arguments
print("\nCase-2:")
productInfo(1200, "Laptop")