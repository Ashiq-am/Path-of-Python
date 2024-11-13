def greet(name, /, message):
	return f"Hello, {name}! {message}"

# Call the function using positional arguments
result = greet("Geeks", "How are you?")
print(result)
