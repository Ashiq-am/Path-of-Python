# Python3 code to demonstrate
# interval initializing in list
# using list comprehension + enumerate()

# initializing lists
test_list = list(range(50))

# printing original list
print("The original list is : " + str(test_list))

# interval elements
N = 5

# interval difference
K = 15

# using list comprehension + enumerate()
# interval initializing in list
res = [i for j, i in enumerate(test_list) if j % K < N]

# printing result
print("The modified initialized list : " + str(res))
