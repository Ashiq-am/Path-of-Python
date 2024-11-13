# Python3 code to demonstrate
# Kth Number digit match
# using list comprehension + all()

# initializing list
test_list = [467, 565, 2645, 8668]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 1

# using list comprehension + all()
# Kth Number digit match
res = all(str(i)[K] == str(test_list[K])[K] for i in test_list)

# print result
print("Does each element of index K have same digit ? " + str(res))
