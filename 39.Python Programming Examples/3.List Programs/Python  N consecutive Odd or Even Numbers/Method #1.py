# Python3 code to demonstrate
# N consecutive Odd or Even Numbers
# using sum() + zip() + any() + list comprehension

# initializing list
test_list = [1, 5, 6, 4, 8]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 3

# using sum() + zip() + any() + list comprehension
# N consecutive Odd or Even Numbers
temp = ( test_list[i : i + N] for i in range(len(test_list) - N + 1) )
res = any( sum(ele % 2 for ele in temps) % N == 0 for temps in temp )

# print result
print("Does list contain the desired consecution : " + str(res))
