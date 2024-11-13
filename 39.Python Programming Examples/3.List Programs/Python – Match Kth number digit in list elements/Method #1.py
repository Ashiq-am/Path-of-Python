# Python3 code to demonstrate
# Kth Number digit match
# using list comprehension + map()

# initializing list
test_list = [467, 565, 2645, 8668]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 1

# using list comprehension + map()
# Kth Number digit match
res = len(set(sub[K] for sub in map(str, test_list))) == 1

# print result
print("Does each element of index K have same digit ? " + str(res))
