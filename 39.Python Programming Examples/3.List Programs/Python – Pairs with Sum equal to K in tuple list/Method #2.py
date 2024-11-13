# Python3 code to demonstrate
# Pairs with Sum equal to K in tuple list
# using list comprehension

# Initializing list
test_list = [(4, 5), (6, 7), (3, 6), (1, 2), (1, 8)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 9

# Pairs with Sum equal to K in tuple list
# using list comprehension
res = [(ele[0], ele[1]) for ele in test_list if ele[0] + ele[1] == K]

# printing result
print ("List after extracting pairs equal to K : " + str(res))
