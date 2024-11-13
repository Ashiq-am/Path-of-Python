# Python3 code to demonstrate working of
# Render Initials as Dictionary Key
# Using loop

# initializing list
test_list = ["geeksforgeeks", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

res = dict()
for ele in test_list:
    # assigning initials as key
    res[ele[0]] = ele

# printing result
print("Constructed Dictionary : " + str(res))
