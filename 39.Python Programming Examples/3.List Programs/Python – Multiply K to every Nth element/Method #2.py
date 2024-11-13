# Python3 code to demonstrate
# Multiply K to every Nth element
# using list comprehension + list slicing

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# initializing N
N = 3

# initializing K
K = 2

# using list comprehension + list slicing
# Multiply K to every Nth element
test_list[0::3] = [i * K for i in test_list[0 :: N]]

# printing result
print ("The list after multiplying K to every Nth element : "
											+ str(test_list))
