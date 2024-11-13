# Python3 code to demonstrate
# Numeric Sort in Mixed Pair String List
# using split() + sorted() + lambda

# Initializing list
test_list = ["Manjeet 5", "Akshat 7", "Akash 6", "Nikhil 10"]

# printing original list
print("The original list is : " + str(test_list))

# Numeric Sort in Mixed Pair String List
# using split() + sorted() + lambda
res = sorted(test_list, reverse = True, key = lambda ele: int(ele.split()[1]))

# printing result
print ("The reverse sorted numerics are : " + str(res))
