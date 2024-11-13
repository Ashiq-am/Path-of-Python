# Python3 code to demonstrate working of
# Record Point with Minimum difference
# Using list comprehension + min()

# initialize list
test_list = [(3, 5), (1, 7), (10, 3), (1, 2)]

# printing original list
print("The original list : " + str(test_list))

# Record Point with Minimum difference
# Using list comprehension + min()
temp = [abs(b - a) for a, b in test_list]
res = min(temp)

# printing result
print("Minimum difference among pairs : " + str(res))
