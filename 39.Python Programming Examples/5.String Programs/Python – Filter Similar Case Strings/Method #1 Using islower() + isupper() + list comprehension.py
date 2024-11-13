# Python3 code to demonstrate working of
# Filter Similar Case Strings
# Using islower() + isupper() + list comprehension

# initializing Matrix
test_list = ["GFG", "Geeks",
             "best", "FOr", "all", "GEEKS"]

# printing original list
print("The original list is : " + str(test_list))

# islower() and isupper() used to check for cases
res = [sub for sub in test_list if sub.islower() or sub.isupper()]

# printing result
print("Strings with same case : " + str(res))
