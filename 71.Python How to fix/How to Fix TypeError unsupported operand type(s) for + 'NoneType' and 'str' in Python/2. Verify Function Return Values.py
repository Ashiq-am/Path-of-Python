def get_string():
    return "Hello"
result = get_string() + " World"
print(result)  # Output: Hello World
# Handling None return
def get_optional_string():
    return None
result = get_optional_string()
if result is not None:
    result += " World"
else:
    result = "Default String"
print(result)  # Output: Default String
