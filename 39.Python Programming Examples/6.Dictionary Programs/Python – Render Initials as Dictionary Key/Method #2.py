# Python3 code to demonstrate working of
# Render Initials as Dictionary Key
# Using dictionary comprehension

# initializing list
test_list = ["geeksforgeeks", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# constructing dictionary
res = {ele[0] : ele for ele in test_list}

# printing result
print("Constructed Dictionary : " + str(res))
