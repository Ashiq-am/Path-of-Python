# Python3 code to demonstrate working of
# Filter Similar Case Strings
# Using islower() + isupper() + filter() + lambda

# initializing Matrix
test_list = ["GFG", "Geeks", "best",
             "FOr", "all", "GEEKS"]

# printing original list
print("The original list is : " + str(test_list))

# islower() and isupper() used to check for cases
# filter() and lambda function used for filtering
res = list(filter(lambda sub: sub.islower() or sub.isupper(), test_list))

# printing result
print("Strings with same case : " + str(res))
