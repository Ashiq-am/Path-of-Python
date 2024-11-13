# Python3 code to demonstrate
# Rear elements Average in List
# using list comprehension + sum()

# Initializing list
test_list = [5, 6, 4, 7, 8, 1, 10]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 3

# Rear elements Average in List
# using list comprehension + sum()
res = test_list[ : K] + [sum(test_list[K:]) / len(test_list[K: ])]

# printing result
print ("Average List after K elements : " + str(res))
