# initializing list
test_list = ["geeksforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing char range
strt, end = 14, 30

# strt and end used to get desired characters
res = ''.join([sub for sub in test_list])[strt : end]

# printing result
print("Range characters : " + str(res))
