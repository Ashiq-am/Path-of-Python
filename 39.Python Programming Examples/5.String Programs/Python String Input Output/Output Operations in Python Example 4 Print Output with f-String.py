# Define variables
name = "Rahul"
age = 30
height = 175.5

# Using format string
print("Name: {}, Age: {}, Height: {}".format(name, age, height))

# Using f-string (Python 3.6+)
print(f"Name: {name}, Age: {age}, Height: {height}")

# Using format string with formatting options
print("Name: {:10s}, Age: {:3d}, Height: {:.2f}".format(name, age, height))
