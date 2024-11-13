# Python3 code to demonstrate working of
# Difference between Uni length slicing and Access Notation
# No Index out of bounds Exception in case of Slice operation

# initializing lists
test_list = [5, 7, 2, 6, 8, 1]

# printing string
print("The original list : " + str(test_list))

# access Notation results
try:
    acc_list = test_list[17]
except Exception as e:
    acc_list = str(e)

# unilength slicing results
slc_list = test_list[17: 18]

# printing results
print("The access notation result for list : " + str(acc_list))
print("The slicing result for list : " + str(slc_list))
