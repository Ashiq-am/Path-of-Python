# Python3 code to demonstrate working of
# Test for Unique Frequencies
# Using loop + set()

# initializing list
test_list = [4, 3, 2, 2, 3, 4, 4, 4, 1, 2]

# printing original list
print("The original list : " + str(test_list))

# Test for Unique Frequencies
res = False
temp = [0] * 5
for ele in test_list:
    # performing memoization in temp list
    temp[ele] += 1
mem_list = temp[1:]

# checking for set converted list length with original list
if len(list(set(mem_list))) == len(mem_list):
    res = True

# printing result
print("Are element's Frequencies Unique ? : " + str(res))
