# Python3 code to demonstrate working of
# Extract Symmetric Tuples
# Using dictionary comprehension + set()

# initializing list
test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Extract Symmetric Tuples
# Using dictionary comprehension + set()
temp = set(test_list) & {(b, a) for a, b in test_list}
res = {(a, b) for a, b in temp if a < b}

# printing result
print("The Symmetric tuples : " + str(res))
