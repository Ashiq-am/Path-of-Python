# Python3 code to demonstrate working of
# Assigning Key values to list elements from Value list Dictionary
# Using dictionary comprehension + list comprehension

# initializing list
test_list = [4, 6, 3, 10, 5, 3]

# printing original list
print("The original list : " + str(test_list))

# initializing dictionary
test_dict = {"Gfg" : [5, 3, 6], "is" : [8, 4], "Best" : [10, 11]}

# creating inverse dictionary of elements
temp = {j : i for i, k in test_dict.items() for j in k}

# creating end result by mapping elements
res = [temp.get(key) for key in test_list]

# printing result
print("The filtered list : " + str(res))
