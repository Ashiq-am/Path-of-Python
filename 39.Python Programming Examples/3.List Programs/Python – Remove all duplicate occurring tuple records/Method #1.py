# Python3 code to demonstrate working of
# Remove all Duplicate occurring records
# Using list comprehension + set() + count()

# initialize list
test_list = [(3, 4), (4, 5), (3, 4), (3, 6), (4, 5), (6, 7)]

# printing original list
print("The original list : " + str(test_list))

# Remove all Duplicate occurring records
# Using list comprehension + set() + count()
res = list(set([ele for ele in test_list if not test_list.count(ele) > 1]))

# printing result
print("All the non Duplicate from list are : " + str(res))
