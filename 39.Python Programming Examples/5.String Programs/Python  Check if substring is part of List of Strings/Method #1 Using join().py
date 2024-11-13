# Python3 code to demonstrate working of
# Check if substring is part of List of Strings
# Using join()

# initializing list
test_list = ['GeeksforGeeks', 'is', 'Best']

# test string
check_str = "for"

# printing original string
print("The original string is : " + str(test_list))

# Using join()
# Check if substring is part of List of Strings
temp = '\t'.join(test_list)
res = check_str in temp

# printing result
print("Is check string part of any input list string : " + str(res))
