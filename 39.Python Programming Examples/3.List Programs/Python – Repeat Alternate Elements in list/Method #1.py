# Python3 code to demonstrate
# Alternate Element Repetition
# using list comprehension

# initializing list of lists
test_list = [4, 5, 6]

# printing original list
print("The original list : " + str(test_list))

# declaring magnitude of repetition
K = 3

# using list comprehension
# Alternate Element Repetition
res = [ele for idx, ele in enumerate(test_list) for i in range(K) if idx % 2 == 0]

# printing result
print("The list after alternate repeating elements : " + str(res))
