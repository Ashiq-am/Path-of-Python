# Python3 code to demonstrate working of
# Add list elements to tuples list
# Using list comprehension + "+" operator

# initializing list
test_list = [(5, 6), (2, 4), (5, 7), (2, 5)]

# printing original list
print("The original list is : " + str(test_list))

# initializing list
sub_list = [7, 2, 4, 6]

# Add list elements to tuples list
# Using list comprehension + "+" operator
res = [sub + tuple(sub_list) for sub in test_list]

# printing result
print("The modified list : " + str(res))
