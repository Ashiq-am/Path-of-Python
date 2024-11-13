# Python3 code to demonstrate
# Remove Record if Nth Column is K
# using list comprehension

# Initializing list
test_list = [(5, 7), (6, 7, 8), (7, 8, 10), (7, 1)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 7

# Initializing N
N = 1

# Remove Record if Nth Column is K
# using list comprehension
res = [sub for sub in test_list if sub[N] != K]

# printing result
print ("List after removal : " + str(res))
