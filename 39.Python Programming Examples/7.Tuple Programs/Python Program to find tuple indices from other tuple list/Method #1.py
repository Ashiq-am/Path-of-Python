# Python3 code to demonstrate working of
# Find tuple indices from other tuple list
# Using lookup dictionary + enumerate() + list comprehension

# initializing list
test_list = [(4, 5), (7, 6), (1, 0), (3, 4)]

# printing original list
print("The original list is : " + str(test_list))

# initializing search tuple
search_tup = [(3, 4), (8, 9), (7, 6), (1, 2)]

# creating lookup_dict
lookup_dict = {val: key for key, val in enumerate(test_list)}

# creating result list
res = [lookup_dict[idx] for idx in search_tup if idx in lookup_dict]

# printing result
print("The match tuple indices : " + str(res))
