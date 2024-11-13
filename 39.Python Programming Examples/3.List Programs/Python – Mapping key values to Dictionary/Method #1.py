# Python3 code to demonstrate working of
# Mapping key values to Dictionary
# Using dictionary comprehension

# initializing list
test_list = [{'name' : 'Manjeet', 'age' : 23},
			{'name' : 'Akshat', 'age' : 22},
			{'name' : 'Nikhil', 'age' : 21}]

# printing original list
print("The original list is : " + str(test_list))

# Mapping key values to Dictionary
# Using dictionary comprehension
res = {sub['name'] : sub['age'] for sub in test_list}

# printing result
print("The flattened dictionary is : " + str(dict(res)))
