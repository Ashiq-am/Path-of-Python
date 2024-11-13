# Python3 code to demonstrate
# Storing Elements Greater than K as Dictionary
# using dictionary comprehension

# Initializing list
test_list = [12, 44, 56, 34, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 50

# Storing Elements Greater than K as Dictionary
# using dictionary comprehension
res = {idx: ele for idx, ele in enumerate(test_list) if ele >= K}

# printing result
print("The dictionary after storing elements : " + str(res))
