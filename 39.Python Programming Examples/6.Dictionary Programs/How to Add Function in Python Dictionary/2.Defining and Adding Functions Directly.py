def greet():
    return "Hello, world!"

my_dict = {
    'greet': greet
}

# Calling the function stored in the dictionary
print(my_dict['greet']())  # Output: Hello, world!
