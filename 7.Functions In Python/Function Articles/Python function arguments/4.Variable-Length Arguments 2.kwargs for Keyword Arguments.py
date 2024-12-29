def print_details(**kwargs):
    # Iterates over keyword arguments and prints each key-value pair
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Harshit", age=25, city="New Delhi")