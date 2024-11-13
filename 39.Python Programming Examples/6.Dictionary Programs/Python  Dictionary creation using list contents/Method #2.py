# Python3 code to demonstrate
# Dictionary creation using list contents
# using dictionary comprehension + enumerate()

# initializing list
keys_list = ["key1", "key2"]
nested_name = ["Manjeet", "Nikhil"]
nested_age = [22, 21]

# printing original lists
print("The original key list : " + str(keys_list))
print("The original nested name list : " + str(nested_name))
print("The original nested age list : " + str(nested_age))

# using dictionary comprehension + enumerate()
# Dictionary creation using list contents
res = {val : {"name": nested_name[key], "age": nested_age[key]}
	for key, val in enumerate(keys_list)}

# print result
print("The dictionary after construction : " + str(res))
