def greet(name):
    print(f"Hello, {name}!")

# Call the function with initial parameters
greet("Alice")

# Modify the function
greet = lambda name: print(f"Hi there, {name}!")

# Recalling the modified function
greet("Bob")