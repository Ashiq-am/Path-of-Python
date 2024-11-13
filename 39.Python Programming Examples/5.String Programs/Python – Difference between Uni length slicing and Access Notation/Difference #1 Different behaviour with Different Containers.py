# Python3 code to demonstrate working of
# Difference between Uni length slicing and Access Notation
# In different containers

# initializing lists
test_list = [5, 7, 2, 6, 8, 1]

# initializing string
test_str = "572681"

# printing original list
print("The original list : " + str(test_list))

# printing string
print("The original string : " + str(test_str))
print("\r")

# access Notation results
acc_list = test_list[3]
acc_str = test_str[3]

# unilength slicing results
slc_list = test_list[3 : 4]
slc_str = test_str[3 : 4]

# printing results
print("The access notation result for list : " + str(acc_list))
print("The access notation result for string : " + str(acc_str))
print("\r")
print("The slicing result for list : " + str(slc_list))
print("The slicing result for string : " + str(slc_str))
