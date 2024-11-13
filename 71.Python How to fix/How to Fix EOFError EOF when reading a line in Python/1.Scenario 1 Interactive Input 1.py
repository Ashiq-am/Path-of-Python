try:
    name = input("Enter your name: ")
except EOFError:
    name = "default_name"
print(f"Hello, {name}!")
