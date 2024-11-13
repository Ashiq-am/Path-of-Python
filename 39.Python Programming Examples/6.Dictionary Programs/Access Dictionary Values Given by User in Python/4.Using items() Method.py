user_dict ={'name': 'geeks', 'age': 21, 'country': 'India'}
key = input("Enter a key: ")

for k, v in user_dict.items():
	if k == key:
		print(f"The value for key '{key}' is: {v}")
		break
else:
	print(f"Key '{key}' not found in the dictionary.")
