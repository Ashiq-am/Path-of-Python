# Python3 code to demonstrate
# Get Kth element till N
# using list comprehension + list slicing

# initializing list
test_list = [['Geeks', 1, 15], ['for', 3, 5], ['Geeks', 3, 7]]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 2

# initializing K
K = 1

# using list comprehension + list slicing
# Get Kth element till N
res = [i[K] for i in test_list[ : N]]

# print result
print("The Kth element of sublist till N : " + str(res))
