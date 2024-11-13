# Python3 code to demonstrate working of
# Adding comma between numbers
# Using format()

# initializing number
test_num = 1234567

# printing original number
print("The original number is : " + str(test_num))

# Using format()
# Adding comma between numbers
res = (format (test_num, ', d'))

# printing result
print("The number after inserting commas : " + str(res))
