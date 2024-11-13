from collections import defaultdict

user_dict ={'name': 'geeks', 'age': 21, 'country': 'India'}
key = input("Enter a key: ")

default_dict = defaultdict(lambda: "Key not found", user_dict)
value = default_dict[key]
print(f"The value for key '{key}' is: {value}")
