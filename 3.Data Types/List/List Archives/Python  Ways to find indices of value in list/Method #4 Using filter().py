# Python3 code to demonstrate
# finding indices of values
# using filter()

# initializing list
test_list = [1, 3, 4, 3, 6, 7]

# printing initial list
print("Original list : " + str(test_list))

# using filter()
# to find indices for 3
res_list = list(filter(lambda x: test_list[x] == 3, range(len(test_list))))

# printing resultant list
print("New indices list : " + str(res_list))
