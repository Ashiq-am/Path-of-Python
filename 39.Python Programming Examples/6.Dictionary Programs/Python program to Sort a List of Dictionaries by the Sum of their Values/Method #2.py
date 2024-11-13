# Python3 code to demonstrate working of
# Sort Dictionaries by Values Sum
# Using sorted() + lambda + sum() + values()

# initializing list
test_list = [{1 : 3, 4 : 5, 3 : 5}, {1 : 7, 10 : 1, 3 : 10}, {1 : 100}, {8 : 9, 7 : 3}]

# printing original list
print("The original list is : " + str(test_list))

# lambda function to get values sum
res = sorted(test_list, key = lambda row : sum(list(row.values())))

# printing result
print("Sorted Dictionaries List : " + str(res))
