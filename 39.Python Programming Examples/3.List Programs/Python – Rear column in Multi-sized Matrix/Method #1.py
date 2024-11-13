# Python3 code to demonstrate working of
# Rear column in Multisized Matrix
# Using loop

# initializing list
test_list = [[3, 4, 5], [7], [8, 4, 6, 1], [10, 3]]

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub in test_list:
    # getting rear element using "-1"
    res.append(sub[-1])

# printing results
print("Filtered column : " + str(res))
