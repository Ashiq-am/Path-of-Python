# Python3 code to demonstrate
# Rear elements Average in List
# using list comprehension + mean()
from statistics import mean

# Initializing list
test_list = [5, 6, 4, 7, 8, 1, 10]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 3

# Rear elements Average in List
# using list comprehension + mean()
res = [*test_list[:K], mean(test_list[K:])]

# printing result
print ("Average List after K elements : " + str(res))
