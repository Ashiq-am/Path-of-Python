# Python3 code to demonstrate
# finding indices of values
# using list comprehension

# initializing list
test_list = [1, 3, 4, 3, 6, 7]

# printing initial list
print("Original list : " + str(test_list))

# using list comprehension
# to find indices for 3
res_list = [i for i in range(len(test_list)) if test_list[i] == 3]

# printing resultant list
print("New indices list : " + str(res_list))
