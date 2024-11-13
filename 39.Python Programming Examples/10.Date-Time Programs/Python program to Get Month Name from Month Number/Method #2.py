# Python3 code to demonstrate working of
# Get Month Name from Month Number
# Using calendar library and month number
import calendar

# initializing month number
test_num = 5

# printing original month number
print("The original month number is : " + str(test_num))

# using month_name() to get month name
res = calendar.month_name[test_num]

# printing result
print("Month Name from Number : " + str(res))
