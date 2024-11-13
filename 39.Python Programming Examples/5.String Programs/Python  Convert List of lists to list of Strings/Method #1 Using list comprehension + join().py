# Python3 code to demonstrate working of
# Convert List of lists to list of Strings
# using list comprehension + join()

# initialize list
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]

# printing original list
print("The original list : " + str(test_list))

# Convert List of lists to list of Strings
# using list comprehension + join()
res = [''.join(ele) for ele in test_list]

# printing result
print("The String of list is : " + str(res))
