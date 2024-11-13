# Python3 code to demonstrate working of
# All possible pairs in List
# Using list comprehension + enumerate()

# initializing list
test_list = [1, 7, 4, 3]

# printing original list
print("The original list : " + str(test_list))

# All possible pairs in List
# Using list comprehension + enumerate()
res = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]

# printing result
print("All possible pairs : " + str(res))
