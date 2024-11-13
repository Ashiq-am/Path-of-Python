# Python3 code to demonstrate working of
# Extract elements with equal frequency as value
# Using filter() + lambda + count()

# initializing list
test_list = [4, 3, 2, 2, 3, 4, 1, 3, 2, 4, 4]

# printing original list
print("The original list is : " + str(test_list))

# removing duplicates using set()
# count() for computing frequency
# filter used to perform filtering
res = list(set(list(filter(lambda ele : test_list.count(ele) == ele, test_list))))

# printing result
print("Filtered elements : " + str(res))
