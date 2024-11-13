# Python3 code to demonstrate working of
# K elements Reversed Slice
# Using list slicing

# initializing list
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 6

# using double slice to solve problem.
# "-" sign for slicing from rear
res = test_list[-K:][::-1]

# printing result
print("The sliced list : " + str(res))
