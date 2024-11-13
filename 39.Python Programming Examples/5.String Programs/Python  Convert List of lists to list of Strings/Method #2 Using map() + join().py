# Python3 code to demonstrate working of
# Convert List of lists to list of Strings
# using map() + join()

# initialize list
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]

# printing original list
print("The original list : " + str(test_list))

# Convert List of lists to list of Strings
# using map() + join()
res = list(map(''.join, test_list))

# printing result
print("The String of list is : " + str(res))
