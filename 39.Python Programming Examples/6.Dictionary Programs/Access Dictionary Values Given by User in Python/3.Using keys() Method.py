user_dict = {'name': 'geeks', 'age': 21, 'country': 'India'}
key = input("Enter a key: ")

if key in user_dict.keys():
	value = user_dict[key]
	print(f"The value for key '{key}' is: {value}")
else:
	print(f"Key '{key}' not found in the dictionary.")
