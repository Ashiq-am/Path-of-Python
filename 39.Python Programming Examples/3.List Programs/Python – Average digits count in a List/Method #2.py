# Python3 code to demonstrate working of
# Average digits count
# Using len() + sum() + str()

# initializing list
test_list = [34, 2345, 23, 456, 2, 23, 456787]

# printing original list
print("The original list is : " + str(test_list))

# getting summation and dividing by total length
res = sum([len(str(ele)) for ele in test_list]) / len(test_list)

# printing result
print("Average digits length " + str(res))
