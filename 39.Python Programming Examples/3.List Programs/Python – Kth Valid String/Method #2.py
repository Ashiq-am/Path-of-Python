# Python code to demonstrate
# Kth Valid String
# using filter()

# initializing list
test_list = ["", "", "Akshat", "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# using filter()
# Kth Valid String
res = filter(None, test_list)[K - 1]

# printing result
print("The Kth non empty string is : " + str(res))
