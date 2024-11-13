# Python3 code to demonstrate working of
# Sort list of Single Item dictionaries according to custom ordering
# Using sorted() + index() + keys() + lambda

# initializing lists
test_list1 = [{'is' : 4}, {'for' : 7}, {"Gfg" : 10}, {"Best" : 1}, {"CS" : 8}]
test_list2 = ["Gfg", "is", "Best", "for", "CS"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# sorted() used to perform sort(), returns the result
# to other variable, ordering handled using index() from order list
res = sorted(test_list1, key = lambda ele: test_list2.index(list(ele.keys())[0]))

# printing result
print("The custom order list : " + str(res))
