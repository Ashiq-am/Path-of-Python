# Python3 code to demonstrate working of
# Sort Strings By Substring Range
# Using lambda function + sort() + slicing

# initializing list
test_list = ["geeksforgeeks", "best", "geeks", "preparation"]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 1, 3

# lambda function providing sort fnc.
test_list.sort(key=lambda test_str : test_str[i : j])

# printing result
print("Strings after sorting : " + str(test_list))
