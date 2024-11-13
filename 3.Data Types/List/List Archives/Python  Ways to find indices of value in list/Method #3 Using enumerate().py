# Python3 code to demonstrate
# finding indices of values
# using enumerate()

# initializing list
test_list = [1, 3, 4, 3, 6, 7]

# printing initial list
print("Original list : " + str(test_list))

# using enumerate()
# to find indices for 3
res_list = [i for i, value in enumerate(test_list) if value == 3]

# printing resultant list
print("New indices list : " + str(res_list))
