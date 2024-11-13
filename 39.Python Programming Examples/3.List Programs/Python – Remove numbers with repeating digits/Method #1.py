# Python3 code to demonstrate working of
# Remove numbers with repeting digits
# Using set() + len() + list comprehension

# initializing list
test_list = [4252, 6578, 3421, 6545, 6676]

# printing original list
print("The original list is : " + str(test_list))

# set() used to remove digits
res = [sub for sub in test_list if len(set(str(sub))) == len(str(sub))]

# printing result
print("List after removing repeating digit numbers : " + str(res))
