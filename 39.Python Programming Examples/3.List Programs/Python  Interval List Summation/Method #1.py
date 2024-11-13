# Python3 code to demonstrate
# Interval List Summation
# using list comprehension + enumerate() + sum()

# initializing lists
test_list = list(range(50))

# printing original list
print("The original list is : " + str(test_list))

# interval elements
N = 5

# interval difference
K = 15

# using list comprehension + enumerate() + sum()
# Interval List Summation
res = sum([i for j, i in enumerate(test_list) if j % K < N])

# printing result
print("The modified range sum list : " + str(res))
