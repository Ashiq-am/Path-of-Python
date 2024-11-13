user_dict = {'name': 'geeks', 'age': 21, 'country': 'India'}
key = input("Enter a key: ")

value = user_dict.get(key, "Key not found")
print(f"The value for key '{key}' is: {value}")
