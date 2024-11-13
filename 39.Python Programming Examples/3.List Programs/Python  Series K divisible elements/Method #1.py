# Python3 code to demonstrate
# Series K divisible elements
# using sum() + zip() + any() + list comprehension

# initializing list
test_list = [1, 5, 6, 4, 8, 12]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 3

# initializing K
K = 4

# using sum() + zip() + any() + list comprehension
# Series K divisible elements
temp = ( test_list[i : i + N] for i in range(len(test_list) - N + 1) )
res = any( sum(ele % K for ele in temps) % N == 0 for temps in temp )

# print result
print("Does list contain the desired consecution : " + str(res))
