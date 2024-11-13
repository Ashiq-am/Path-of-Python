# Python3 code to demonstrate
# Separating odd and even index elements
# Using list slicing

# initializing list
test_list = [3, 6, 7, 8, 9, 2, 1, 5]

# printing original list
print("The original list : " + str(test_list))

# Using list slicing
# Separating odd and even index elements
res = test_list[::2] + test_list[1::2]

# print result
print("Seprated odd and even index list : " + str(res))
