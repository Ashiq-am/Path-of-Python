# Python3 code to demonstrate working of
# Extract elements with equal frequency as value
# Using list comprehension + count()

# initializing list
test_list = [4, 3, 2, 2, 3, 4, 1, 3, 2, 4, 4]

# printing original list
print("The original list is : " + str(test_list))

# removing duplicates using set()
# count() for computing frequency
res = list(set([ele for ele in test_list if test_list.count(ele) == ele]))

# printing result
print("Filtered elements : " + str(res))
