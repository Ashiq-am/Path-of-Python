# Python3 code to demonstrate working of
# Filter similar elements Tuples
# Using list comprehension + set() + len()

# initializing list
test_list = [(5, 6, 5, 5), (6, 6, 6), (1, 1), (9, 10)]

# printing original list
print("The original list is : " + str(test_list))

# length is computed using len()
res = [sub for sub in test_list if len(set(sub)) == 1]

# printing results
print("Filtered Tuples : " + str(res))
