# Python3 code to demonstrate working of
# Test if list is Palindrome
# Using reversed()

# initializing list
test_list = [1, 4, 5, 4, 1]

# printing original list
print("The original list is : " + str(test_list))

# reversing list
rev_list = list(reversed(test_list))

# checking for Palindrome
res = rev_list == test_list

# printing result
print("Is list Palindrome : " + str(res))
