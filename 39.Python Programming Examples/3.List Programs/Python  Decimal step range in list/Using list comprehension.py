# Python3 code to demonstrate working of
# Decimal step range in list
# using list comprehension

# initializing start value
strt = 5

# initializing step value
step = 0.4

# using list comprehension
# Decimal step range
test_list = [strt + (x * step) for x in range(0, 5)]

# Printing result
print("The list after decimal range value initialization : " + str(test_list))
