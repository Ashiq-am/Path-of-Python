# Python3 code to demonstrate
# Numeric Sort in Mixed Pair String List
# using split() + sort() + key function

# helper function
def helper_func(ele):
    name, val = ele.split()
    return int(val)


# Initializing list
test_list = ["Manjeet 5", "Akshat 7", "Akash 6", "Nikhil 10"]

# printing original list
print("The original list is : " + str(test_list))

# Numeric Sort in Mixed Pair String List
# using split() + sort() + key function
test_list.sort(key=helper_func, reverse=True)

# printing result
print("The reverse sorted numerics are : " + str(test_list))
