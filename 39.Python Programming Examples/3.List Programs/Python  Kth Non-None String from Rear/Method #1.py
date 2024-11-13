# Python3 code to demonstrate
# Kth Non-None String from Rear
# using next() + list comprehension

# initializing list
test_list = ["", "", "Akshat", "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# using next() + list comprehension
# Kth Non-None String from Rear
test_list.reverse()
test_list = iter(test_list)
for idx in range(0, K):
	res = next(sub for sub in test_list if sub)

# printing result
print("The Kth non empty string from rear is : " + str(res))
