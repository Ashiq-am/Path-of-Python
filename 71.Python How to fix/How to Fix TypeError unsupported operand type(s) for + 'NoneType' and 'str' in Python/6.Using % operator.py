my_string = "Hello, %s"
name = None

greeting = my_string % (name or "Guest")
print(greeting)  # Output: Hello, Guest
