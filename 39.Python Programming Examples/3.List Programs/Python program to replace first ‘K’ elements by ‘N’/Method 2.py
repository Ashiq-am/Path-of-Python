# initializing list
test_list = [3, 4, 6, 8, 4, 2, 6, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# initializing N
N = 6

# assigning the N value till K elements
test_list[: K] = [N] * K

# printing result
print("Elements after replacement : " + str(test_list))
