# Python3 code to demonstrate working of
# Find tuple indices from other tuple list
# Using list comprehension + enumerate()

# initializing list
test_list = [(4, 5), (7, 6), (1, 0), (3, 4)]

# printing original list
print("The original list is : " + str(test_list))

# initializing search tuple
search_tup = [(3, 4), (8, 9), (7, 6), (1, 2)]

# enumerate() gets all the indices
res = [idx for idx, val in enumerate(test_list) for ele in search_tup if ele == val]

# printing result
print("The match tuple indices : " + str(res))
