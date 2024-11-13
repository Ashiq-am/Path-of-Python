# Python3 code to demonstrate working of
# Convert String float to float list
# using list comprehension + split() + float()

# initializing string
test_str = "3.44, 7.8, 9.12, 100.2, 6.50"

# printing original string
print("The original string is : " + test_str)

# Convert String float to float list
# using list comprehension + split() + float()
res = [float(idx) for idx in test_str.split(', ')]

# printing result
print("The float list is : " + str(res))
