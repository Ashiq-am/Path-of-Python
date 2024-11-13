# Python3 code to demonstrate working of
# Matrix Minimum difference in extreme values row
# Using min() + list comprehension

# initializing list
test_list = [[4, 10, 18], [5, 3, 10], [1, 4, 6], [19, 2]]

# printing original list
print("The original list is : " + str(test_list))

# getting min value
min_val = min([max(sub) - min(sub) for sub in test_list])

# using list comprehension to filter
res = [sub for sub in test_list if max(sub) - min(sub) == min_val]

# printing result
print("Rows with Minimum difference in extreme values : " + str(res))
