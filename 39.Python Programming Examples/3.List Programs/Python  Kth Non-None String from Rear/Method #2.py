# Python code to demonstrate
# Kth Non-None String from Rear
# using filter()

# initializing list
test_list = ["", "", "Akshat", "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# using filter()
# Kth Non-None String from Rear
res = filter(None, test_list)[-K]

# printing result
print("The Kth non empty string from rear is : " + str(res))
