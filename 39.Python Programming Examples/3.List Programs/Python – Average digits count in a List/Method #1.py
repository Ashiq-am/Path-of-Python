# Python3 code to demonstrate working of
# Average digits count
# Using len() + loop + str()

# initializing list
test_list = [34, 2345, 23, 456, 2, 23, 456787]

# printing original list
print("The original list is : " + str(test_list))

sumd = 0
for ele in test_list:
    # summing digits length
    sumd += len(str(ele))

# getting result after dividing total digits by elements
res = sumd / len(test_list)

# printing result
print("Average digits length : " + str(res))
