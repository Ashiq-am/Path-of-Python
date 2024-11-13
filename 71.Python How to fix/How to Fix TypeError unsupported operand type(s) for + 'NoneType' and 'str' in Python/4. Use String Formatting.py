my_string = "Hello, {}"
name = None

greeting = my_string.format(name or "Guest")
print(greeting)  # Output: Hello, Guest
