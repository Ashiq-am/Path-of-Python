# Python3 code to demonstrate
# First Non-Empty String in list
# using next() + list comprehension

# initializing list
test_list = ["", "", "Akshat", "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# using next() + list comprehension
# First Non-Empty String in list
res = next(sub for sub in test_list if sub)

# printing result
print("The first non empty string is : " + str(res))
