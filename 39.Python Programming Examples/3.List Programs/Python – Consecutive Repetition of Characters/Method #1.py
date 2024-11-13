# Python3 code to demonstrate working of
# Consecutive Repetition of Characters
# Using list comprehension

# initializing list
test_list = ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# Consecutive Repetition of Characters
# Using list comprehension
res = [sub for ele in test_list for sub in [ele] * K]

# printing result
print("The list after Consecutive Repetition is : " + str(res))
