try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"Caught an error: {e}")
