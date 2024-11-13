# Python3 code to demonstrate working of
# Maximum of Product Pairs in Tuple List
# Using list comprehension + max()

# initialize list
test_list = [(3, 5), (1, 7), (10, 3), (1, 2)]

# printing original list
print("The original list : " + str(test_list))

# Maximum of Product Pairs in Tuple List
# Using list comprehension + max()
temp = [abs(b * a) for a, b in test_list]
res = max(temp)

# printing result
print("Maximum product among pairs : " + str(res))
