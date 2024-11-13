# Python3 code to demonstrate working of
# Sort List by Digits
# Using list comprehension + sorted() + lambda

# initializing list
test_list = [434, 211, 12, 54, 3]

# printing original list
print("The original list is : " + str(test_list))

# performing sort operation
# converting number to list of Digits
res = sorted(test_list, key = lambda ele: [int(j) for j in str(ele)])

# printing result
print("List after sorting : " + str(res))
