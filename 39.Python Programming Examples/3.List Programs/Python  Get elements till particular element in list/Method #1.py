# Python3 code to demonstrate working of
# Get elements till particular element in list
# using index() + list slicing

# initialize list
test_list = [1, 4, 6, 8, 9, 10, 7]

# printing original list
print("The original list is : " + str(test_list))

# declaring elements till which elements required
N = 8

# Get elements till particular element in list
# using index() + list slicing
temp = test_list.index(N)
res = test_list[:temp]

# printing result
print("Elements till N in list are : " + str(res))
