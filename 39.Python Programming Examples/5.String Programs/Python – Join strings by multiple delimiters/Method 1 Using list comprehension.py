# initializing strings
test_str1 = 'Geeksforgeeks'
test_str2 = "Best"

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing join list
join_list = ["+", "*", "-", "$", ",", "@"]

# + operator used for concatenations
res = [test_str1 + delim + test_str2 for delim in join_list]

# printing result
print("All delimiters concatenations : " + str(res))
