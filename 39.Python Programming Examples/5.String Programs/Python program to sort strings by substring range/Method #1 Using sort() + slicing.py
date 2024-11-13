# Python3 code to demonstrate working of
# Sort Strings By Substring Range
# Using sort() + slicing

# helper function
def get_substr(test_str):
    # getting range
    return test_str[i: j]


# initializing list
test_list = ["geeksforgeeks", "best", "geeks", "preparation"]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 1, 3

# calling func.
test_list.sort(key=get_substr)

# printing result
print("Strings after sorting : " + str(test_list))
