my_string = "Hello, "
name = None

greeting = f"{my_string}{name or 'Guest'}"
print(greeting)  # Output: Hello, Guest
