# Python3 code to demonstrate
# Consecutive Custom Chunked elements Product
# using list comprehension + enumerate() + loop

# getting Product
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


# initializing lists
test_list = list(range(1, 50))

# printing original list
print("The original list is : " + str(test_list))

# interval elements
N = 5

# interval difference
K = 15

# using list comprehension + enumerate() + loop
# Consecutive Custom Chunked elements Product
res = prod([i for j, i in enumerate(test_list) if j % K < N])

# printing result
print("The modified range product list : " + str(res))
