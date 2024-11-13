# Python3 code to demonstrate working of
# Test for Unique Frequencies
# Using setdefault() + values()

# initializing list
test_list = [4, 3, 2, 2, 3, 4, 4, 4, 1, 2]

# printing original list
print("The original list : " + str(test_list))

# Test for Unique Frequencies
# Using setdefault() + values()
temp = {}
for ele in test_list:
    # setting default value to 0
    temp.setdefault(ele, 0)
    temp[ele] += 1

# checking for values and keys equality
res = len(set(temp.values())) == len(temp)

# printing result
print("Are element's Frequencies Unique ? : " + str(res))
