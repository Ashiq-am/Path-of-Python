# Python3 code to demonstrate working of
# Sort list of Single Item dictionaries according to custom ordering
# Using sort() + index() + keys() + lambda

# initializing lists
test_list1 = [{'is' : 4}, {'for' : 7}, {"Gfg" : 10}, {"Best" : 1}, {"CS" : 8}]
test_list2 = ["Gfg", "is", "Best", "for", "CS"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# sort() used to perform inplace sort
test_list1.sort(key = lambda ele: test_list2.index(list(ele.keys())[0]))

# printing result
print("The custom order list : " + str(test_list1))
