# Python3 code to demonstrate working of
# remove additional space from string
# Using split() + join()

# initializing string
test_str = "GfG is good		 website"

# printing original string
print("The original string is : " + test_str)

# using split() + join()
# remove additional space from string
res = " ".join(test_str.split())

# printing result
print("The strings after extra space removal : " + str(res))
