# Python3 code to demonstrate working of
# Convert List to delimiter separated String
# Using join() + str()

# initializing list
test_list = [7, "Gfg", 8, "is", "best", 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing delim
delim = "*"

# using map to convert each element to string
temp = list(map(str, test_list))

# join() used to join with delimiter
res = delim.join(temp)

# printing result
print("The resultant string : " + str(res))
