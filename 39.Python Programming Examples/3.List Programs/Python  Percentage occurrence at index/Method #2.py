# Python3 code to demonstrate
# index percentage calculation of element
# using zip() + count() + list comprehension

# initializing test list
test_list = [[3, 4, 5], [2, 4, 6], [3, 5, 4]]

# printing original list
print("The original list : " + str(test_list))

# using zip() + count() + list comprehension
# index percentage calculation of element
res = [sub.count(4)/len(sub) for sub in zip(*test_list)]

# print result
print("The percentage of 4 each index is : " + str(res))
